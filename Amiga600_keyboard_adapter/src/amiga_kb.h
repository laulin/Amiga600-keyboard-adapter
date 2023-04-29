#include <stdint.h>
#define LED1 0x40
#define LED2 0x80
#define LEDS (LED1 | LED2)

void init_kb_reader(void);
uint8_t decode_kb(uint8_t *key, uint8_t key_number);
void display_keys(uint8_t *key, uint8_t key_number);
void write_kb_led(uint8_t led);