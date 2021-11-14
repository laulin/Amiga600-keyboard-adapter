#include <Arduino.h>
#include "spi.h"
//#include "hw_uart.h"
#include <stdint.h>
#include <stdio.h>
#include <util/delay.h>
#include <avr/io.h>
#include "amiga_kb.h"

#define KEYS_SIZE 10
uint8_t keys[KEYS_SIZE] = {0};

void setup()
{
  init_spi();
  //init_hw_uart(baudrate_115200);
  init_kb_reader();
  Serial.begin(115200);
  Serial.println("Test keyboard ready !");
}

// the loop function runs over and over again forever
void loop()
{
  uint8_t read_keys = decode_kb(keys, KEYS_SIZE);
  display_keys(keys, read_keys);
  delay(10);                     // wait for a second
  //Serial.println("Line !");
  //Serial.println(read_keys);
}