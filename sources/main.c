#include "hal.h"
#include <stdint.h>
#include <stdio.h>
#include <util/delay.h>
#include <avr/io.h>
#include "amiga_kb.h"

// example on how to use amiga keyboard decoding

#define KEYS_SIZE 10

int main()
{
    init_spi();
    init_hw_uart(baudrate_115200);
    init_kb_reader();

    uint8_t keys[KEYS_SIZE] = {0};

    while (1)
    {
        uint8_t read_keys = decode_kb(keys, KEYS_SIZE);
        display_keys(keys, read_keys);
        _delay_ms(10);
    }
    
    return 0;
}