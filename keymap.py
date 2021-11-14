import csv
import re

# Convert CSV to C array to create a LUT for raw code to keyboard code

ARRAY_SIZE = 256
lut = [0]*ARRAY_SIZE
labels = ['']*ARRAY_SIZE

with open("keymap.csv") as f:
    reader = csv.reader(f,delimiter=";")
    for i, row in enumerate(reader):
        if i > 0 and len(row) > 2:
            label = row[0]
            raw_code = row[1]
            keyboard_code = row[2]
            # ignore cas of empty string
            if len(keyboard_code) > 0:
                hex_raw_code = re.search(r"0x([0-9a-fA-F]{2,2})", raw_code).group(1)
                dec_raw_code = int(hex_raw_code, 16)
                lut[dec_raw_code] = keyboard_code
                labels[dec_raw_code] = label

lines = [""]*ARRAY_SIZE
for i in range(ARRAY_SIZE):
    code = lut[i];
    label = labels[i]
    if isinstance(code, str) and (len(code) == 1 or code == r"\\"):
        code = f"'{code}'"
    lines[i] = f"    {code} , // {hex(i)} : {label}"

TEMPLATE = """
#include "keymap.h"
#include <Arduino.h>
#include <Keyboard.h>

const uint8_t KEYMAP[{array_size}] = {{
{values}
}};
"""

print(TEMPLATE.format(array_size=ARRAY_SIZE, values="\n".join(lines)))