#ifndef __SPI_HEADER__
#define __SPI_HEADER__

#include <stdint.h>

void init_spi(void);
uint8_t read_write_spi (uint8_t data);
void write_bytes_spi (const uint8_t* data, uint16_t size);
void read_bytes_spi (uint8_t* data, uint16_t size);

void clear_ram0_select(void);
void set_ram0_select(void);
void clear_ram1_select(void);
void set_ram1_select(void);
void clear_rom0_select(void);
void set_rom0_select(void);
void clear_rom1_select(void);
void set_rom1_select(void);
void clear_io_select(void);
void set_io_select(void);
void set_all_select(void);

void write_24bits_address_spi(uint32_t address);

#endif //__SPI_HEADER__