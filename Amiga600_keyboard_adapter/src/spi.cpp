#include "spi.h"
#include <avr/io.h>

#define SPI_DDR DDRB

#define IO_SELECT_PORT PORTC

#define SPI_MOSI_OFFSET (1 << 2)
#define SPI_MISO_OFFSET (1 << 3)
#define SPI_CLK_OFFSET (1 << 1)

// this is an hardware abstraction layer
// can't be unit tester !
// Please care on change, test on board

void init_spi(void)
{
    // set IO as output
    SPI_DDR |= SPI_MOSI_OFFSET | SPI_CLK_OFFSET;
    // SPI_MISO_DDR is unchange, 0/input by default 

    // define SPI master 
    SPCR = (1<<SPE) | (1<<MSTR);
    SPSR = 1<<SPI2X; // you can comment this line to decrease the SPI speed by 2
}

uint8_t read_write_spi (uint8_t data)
{
    // blocking R/W on SPI for one byte
    SPDR = data;
 
    // Wait for byte write/read
    while(!(SPSR & (1<<SPIF) ));
 
    // Return read data
    return SPDR ;
}

void write_bytes_spi (const uint8_t* data, uint16_t size)
{
    uint16_t i=0;
    for(i=0; i< size; i++)
    {
        // blocking R/W on SPI for one byte
        SPDR = data[i];
 
        // Wait for byte write/read
        while(!(SPSR & (1<<SPIF) ));
    }
}

void read_bytes_spi (uint8_t* data, uint16_t size)
{
    uint16_t i=0;
    for(i=0; i< size; i++)
    {
        // write useless data
        SPDR = 0x00;
 
        // Wait for byte write/read
        while(!(SPSR & (1<<SPIF) ));

        data[i] = SPDR;
    }
}