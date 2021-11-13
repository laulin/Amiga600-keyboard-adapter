#include "spi.h"
//#include "hw_uart.h"
#include "port_expander.h"
#include <stdint.h>
#include <stdio.h>
#include <util/delay.h>
#include <avr/io.h>

#define SELECT_DDR DDRB
#define SELECT_PORT PORTB
#define SELECT_0 1
#define SELECT_1 2
#define ENABLE 1
#define DISABLE 0
#define LED1 0x40
#define LED2 0x80
#define LEDS_MASK (LED1 | LED2)

void select_kb(uint8_t chip_index, uint8_t enable)
{
    uint8_t mask = chip_index;
    if (enable == ENABLE)
    {
        SELECT_PORT &= ~chip_index;
    }
    else
    {
        SELECT_PORT |= chip_index;
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
    // set PB0 and PB1 as output and set 1 to each
    SELECT_DDR |= SELECT_0 | SELECT_1;
    SELECT_PORT |= SELECT_0 | SELECT_1;

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
            if (masked == 0 & key_counter < key_number)
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
    uint8_t CLEAR[4] = "\033[2J";
    uint8_t HOME[3] = "\033[H";
    uint8_t buffer[DISPLAY_KEYS_BUFFER_SIZE] = {0};
    uint8_t written = 0;

    if(key_number == 0)
    {
        return;
    }

    // clear the string
    //hw_uart_write_array(CLEAR, 4);
    //hw_uart_write_array(HOME, 3);
    

    for(uint8_t i=0; i< key_number; i++)
    {
        written = snprintf(buffer, DISPLAY_KEYS_BUFFER_SIZE, "0x%x\n", key[i]);
        //hw_uart_write_array(buffer, written);
    }
}