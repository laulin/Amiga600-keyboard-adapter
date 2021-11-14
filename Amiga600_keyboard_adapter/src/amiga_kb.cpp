#include "spi.h"
//#include "hw_uart.h"
#include "port_expander.h"
#include <stdint.h>
#include <stdio.h>
#include <util/delay.h>
#include <avr/io.h>
#include <Arduino.h>

#define SELECT_DDR DDRD
#define SELECT_PORT PORTD
#define SELECT_0 12
#define SELECT_1 9
#define ENABLE 1
#define DISABLE 0
#define LED1 0x40
#define LED2 0x80
#define LEDS_MASK (LED1 | LED2)

void select_kb(uint8_t chip_index, uint8_t enable)
{
    if (enable == ENABLE)
    {
        digitalWrite(chip_index, 0);
    }
    else
    {
        digitalWrite(chip_index, 1);
    }
}

void write_byte_port_expander(uint8_t chip_index, uint8_t address, uint8_t value)
{
    select_kb(chip_index, ENABLE);
    read_write_spi(MSB_ADDR | WRITE_MASK);
    read_write_spi(address);
    read_write_spi(value);
    select_kb(chip_index, DISABLE);
}

uint8_t read_byte_port_expander(uint8_t chip_index, uint8_t address)
{
    uint8_t value = 0;
    select_kb(chip_index, ENABLE);
    read_write_spi(MSB_ADDR | READ_MASK);
    read_write_spi(address);
    value = read_write_spi(0x00);
    select_kb(chip_index, DISABLE);

    return value;
}
// LEDs are on GPB6,7 on chip 1

void write_kb_led(uint8_t led)
{
    write_byte_port_expander(SELECT_1, OLATB, led & LEDS_MASK);
}

void init_kb_reader(void)
{
    pinMode(SELECT_0, OUTPUT);
    pinMode(SELECT_1, OUTPUT);
    digitalWrite(SELECT_0, 1);
    digitalWrite(SELECT_1, 1);

    // set pullup on inputs of chip 0
    write_byte_port_expander(SELECT_0, GPPUA, 0xFF);
    write_byte_port_expander(SELECT_0, GPPUB, 0xFF);

    // set pullup on inputs of chip 1, expect led
    write_byte_port_expander(SELECT_1, GPPUA, 0xFF);
    write_byte_port_expander(SELECT_1, GPPUB, 0xFF ^ LEDS_MASK);

    write_byte_port_expander(SELECT_0, IODIRA, 0xFF);
    write_byte_port_expander(SELECT_0, IODIRB, 0xFF);

    write_byte_port_expander(SELECT_1, IODIRA, 0xFF);
    write_byte_port_expander(SELECT_1, IODIRB, 0xFF ^ LEDS_MASK); // OUTPUT PIN for LEDs
}

uint8_t decode_kb(uint8_t* key, uint8_t key_number)
{
    uint8_t key_counter = 0;

    for (uint16_t i = 0; i < 16; i++)
    {
        uint16_t x = 1 << i;
        uint8_t x_a = x & 0xFF;
        uint8_t x_b = (x >> 8) & 0xFF;

        write_byte_port_expander(SELECT_0, IODIRA, 0xFF ^ x_a);
        write_byte_port_expander(SELECT_0, IODIRB, 0xFF ^ x_b);

        uint8_t y_a = read_byte_port_expander(SELECT_1, GPIOA);
        uint8_t y_b = read_byte_port_expander(SELECT_1, GPIOB) & ~LEDS_MASK;
        uint16_t y = y_a | (y_b << 8);

        for (uint16_t j = 0; j < 14; j++)
        {
            uint16_t mask = 1 << j;
            uint16_t masked = y & mask;
            if ((masked == 0) & (key_counter < key_number))
            {
                uint8_t key_code = i | (j << 4);
                key[key_counter] = key_code;
                key_counter++;
            }
        }
    }

    return key_counter;
}

#define DISPLAY_KEYS_BUFFER_SIZE    16

void display_keys(uint8_t *key, uint8_t key_number)
{
    char CLEAR[6] = "\033[2J\0";
    char HOME[5] = "\033[H\0";
    char buffer[DISPLAY_KEYS_BUFFER_SIZE] = {0};

    if(key_number == 0)
    {
        return;
    }

    // clear the string
    Serial.print(CLEAR);
    Serial.print(HOME);

    for(uint8_t i=0; i< key_number; i++)
    {
        snprintf(buffer, DISPLAY_KEYS_BUFFER_SIZE, "0x%x", key[i]);
        Serial.println(buffer);
    }
}