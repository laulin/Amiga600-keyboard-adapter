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
uint8_t hit = 0;
uint8_t hold = 0;

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
  hit = 0;
  for (uint8_t i = 0; i < read_keys; i++)
  {
    if (keys[i] == 0xBE)
    {
      hit = 1;
    }
  }
  if (hit == 1 && hold == 0)
  {
    Keyboard.press('a');
    Serial.println("Pressed");
    hold = 1;
  }
  if(hit == 0 && hold == 1)
  {
    Keyboard.release('a');
    Serial.println("Release");
    hold = 0;
  }
  //Serial.println("Line !");
  //Serial.println(read_keys);
}