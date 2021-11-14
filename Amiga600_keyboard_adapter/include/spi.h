#ifndef __SPI_HEADER__
#define __SPI_HEADER__

#include <stdint.h>

void init_spi(void);
uint8_t read_write_spi (uint8_t data);
void write_bytes_spi (const uint8_t* data, uint16_t size);
void read_bytes_spi (uint8_t* data, uint16_t size);

#endif //__SPI_HEADER__