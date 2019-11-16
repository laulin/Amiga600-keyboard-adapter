build: setup 
	# need apt install gcc-avr binutils-avr avr-libc avrdude
	# need retroputer HAL installed (https://github.com/laulin/retroputer)
	avr-gcc -Os -std=c11 -DF_CPU=16000000UL -mmcu=atmega328p -I sources/ -I /usr/local/include/retroputer/hal -c -o output/main.o sources/main.c
	avr-gcc -Os -std=c11 -DF_CPU=16000000UL -mmcu=atmega328p -I sources/ -I /usr/local/include/retroputer/hal -c -o output/amiga_kb.o sources/amiga_kb.c
	avr-gcc -mmcu=atmega328p -L"/usr/local/lib/retroputer/hal" -o output/main.bin output/main.o output/amiga_kb.o -lhal
	avr-objcopy -O ihex -R .eeprom output/main.bin output/main.hex 

upload: build
	sudo avrdude -F -V -c arduino -p ATMEGA328P -P /dev/ttyACM0 -b 115200 -U flash:w:output/main.hex

setup:
	mkdir -p output/

clean:
	rm -f output