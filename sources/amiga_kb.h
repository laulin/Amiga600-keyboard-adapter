#include <stdint.h>
void init_kb_reader(void);
uint8_t decode_kb(uint8_t *key, uint8_t key_number);
void display_keys(uint8_t *key, uint8_t key_number);