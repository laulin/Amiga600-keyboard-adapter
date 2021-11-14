#include <Arduino.h>
#include "spi.h"
//#include "hw_uart.h"
#include <stdint.h>
#include <stdio.h>
#include <util/delay.h>
#include <avr/io.h>
#include "amiga_kb.h"
#include <Keyboard.h>

#define KEYS_SIZE 10
uint8_t keys[KEYS_SIZE] = {0};
#define STATE_SIZE 0xE0
#define KEY_HIT 0x01
#define KEY_HOLD 0x02
uint8_t state[STATE_SIZE] = {0};

void reset_state_hit()
{
  for (uint8_t i = 0; i < STATE_SIZE; i++)
  {
    state[i] = state[i] & (~KEY_HIT);
  }
}

void set_state_hit(uint8_t code)
{
  state[code] |= KEY_HIT;
}

void update_state(void (*press)(uint8_t code), void (*release)(uint8_t code))
{
  for (uint8_t code = 0; code < STATE_SIZE; code++)
  {
    uint8_t s = state[code];
    if (s == KEY_HIT)
    {
      state[code] = KEY_HOLD;
      press(code);

    }
    if (s == KEY_HOLD)
    {
      state[code] = 0;
      release(code);
    }
  }
}

void press_key(uint8_t code)
{
  Serial.print("Press ");
  Serial.println(code);
}

void release_key(uint8_t code)
{
  Serial.print("Releases ");
  Serial.println(code);
}

void setup()
{
  init_spi();
  //init_hw_uart(baudrate_115200);
  init_kb_reader();
  Serial.begin(115200);
  Serial.println("Test keyboard ready !");
  Keyboard.begin();
}

// the loop function runs over and over again forever
void loop()
{
  uint8_t read_keys = decode_kb(keys, KEYS_SIZE);
  //display_keys(keys, read_keys);
  delay(10);
  reset_state_hit();
  for (uint8_t i = 0; i < read_keys; i++)
  {
    set_state_hit(keys[i]);
  }
  update_state(press_key, release_key);
}