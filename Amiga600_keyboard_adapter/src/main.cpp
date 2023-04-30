#include <Arduino.h>
#include "spi.h"
#include <stdint.h>
#include <stdio.h>
#include <util/delay.h>
#include <avr/io.h>
#include "amiga_kb.h"
#include <string.h>

#define KEYS_SIZE 16*14
uint8_t keys[KEYS_SIZE] = {0};
#define HEADER_SIZE  3
const char * HEADER = "KBN";
#define LENGTH_SIZE (1)
#define OUTPUT_SIZE (KEYS_SIZE + HEADER_SIZE + LENGTH_SIZE) 
uint8_t output[OUTPUT_SIZE] = {0};
#define HEADER_OFFSET 0
#define LENGTH_OFFSET (HEADER_OFFSET + HEADER_SIZE)
#define DATA_OFFSET (LENGTH_OFFSET + LENGTH_SIZE)

const unsigned long interval = 1000; 
unsigned long previousMicros = 0;

void setup()
{
  init_spi();
  init_kb_reader();
  Serial.begin(460800);
  memcpy(&output[HEADER_OFFSET], HEADER, HEADER_SIZE);
}

// the loop function runs over and over again forever
void loop()
{
  previousMicros = micros();
  uint8_t read_keys = decode_kb(keys, KEYS_SIZE);
  output[LENGTH_OFFSET] = read_keys;
  memcpy(&output[DATA_OFFSET], keys, read_keys);

  Serial.write(output, HEADER_SIZE + LENGTH_SIZE + read_keys);

  while (micros() - previousMicros < interval)
  {

  }
}