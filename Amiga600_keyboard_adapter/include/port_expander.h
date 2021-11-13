#ifndef __PORT_EXPANDER_HEADER__
#define __PORT_EXPANDER_HEADER__

#include <stdint.h>
#include "spi.h"
#include "error.h"

// required : SPI HAL must be init

// with BANK = 0, 16 bits mode
#define IODIRA   0x00        // 1 for input, 0 for output, default is 1
#define IODIRB   0x01        // 1 for input, 0 for output, default is 1
#define GPPUA    0x0C        // 1 set pull up (only on input)
#define GPPUB    0x0D        // 1 set pull up (only on input)
#define GPIOA    0x12        // for read
#define GPIOB    0x13        // for read
#define OLATA    0x14        // for write
#define OLATB    0x15        // for write

// for the first byte
#define MSB_ADDR    0x40
#define WRITE_MASK  0x00
#define READ_MASK   0x01

// port A if for leds (bits 4, 5, 6, 7)
// Bits 0, 1, 2, 3 must stay as input due to a hardware bug
#define IODIRA_VALUE  0x0F
// IODIRB is define by the user

#define LEDA    0
#define LEDB    1
#define LEDC    2
#define LEDD    3

void init_port_expander(void);

void set_led(uint8_t index);
void clear_led(uint8_t index);
void toggle_led(uint8_t index);

#endif // __PORT_EXPANDER_HEADER__