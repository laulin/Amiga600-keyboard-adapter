import logging
import time

import serial
import serial.serialutil
from pynput.keyboard import Controller
from pynput.keyboard import Key


UK_LABELS = {
    0xDF : "esc",
    0xDD : "F1",
    0xDC : "F2",
    0xDB : "F3",
    0xDA : "F4",
    0xD9 : "F5",
    0xD7 : "F6",
    0xD5 : "F7",
    0xD4 : "F8",
    0xD3 : "F9",
    0xD2 : "F10",
    0xD1 : "help",
    0xCF : "tild",
    0xCE : "1",
    0xCD : "2",
    0xCC : "3",
    0xCB : "4",
    0xCA : "5",
    0xC9 : "6",
    0xC8 : "7",
    0xC7 : "8",
    0xC6 : "9",
    0xC5 : "0",
    0xC4 : "-",
    0xC3 : "=",
    0xC2 : "\\",
    0x72  : "backspace",
    0x92 : "del",
    0xBF : "tab",
    0xBE : "q",
    0xBD : "w",
    0xBC : "e",
    0xBB : "r",
    0xBA : "t",
    0xB9 : "y",
    0xB8 : "u",
    0xB7 : "i",
    0xB6 : "o",
    0xB5 : "p",
    0xB4 : "[",
    0xB3 : "]",
    0xB2 : "enter",
    0x30 : "ctrl",
    0x9F : "caps_locks",
    0x9E : "a",
    0x9D : "s",
    0x9C : "d",
    0x9B : "f",
    0x9A : "g",
    0x99 : "h",
    0x98 : "j",
    0x97 : "k",
    0x96 : "l",
    0x95 : ";",
    0x94 : "#",
    0x93 : "void_right",
    0x20 : "shift_left",
    0x7F : "void_left",
    0x7E : "z",
    0x7D : "x",
    0x7C : "c",
    0x7B : "v",
    0x7A : "b",
    0x79 : "n",
    0x78 : "m",
    0x77 : ",",
    0x76 : ".",
    0x75 : "/",
    0x80 : "shift_right",
    0xC1 : "up",
    0x10 : "alt_left",
    0x00 : "amiga_left",
    0x73 : "space",
    0x40 : "amiga_right",
    0x60 : "alt_right",
    0xB1 : "left",
    0x71 : "down",
    0x91 : "right"
}

SHIFT = 1
ALT = 2
AMIGA_RIGHT = 4
AMIGA_LEFT = 8
CTRL = 16
CAPS_LOCKS = 32
VOID = 0

DEFAULT_MASK = VOID | SHIFT
NO_MOD_MASK = VOID


UK_KEYMAP = {
    "tild":{
        SHIFT:{"value" : "`"},
        VOID:{"value" : "~"},
        "key_mask":DEFAULT_MASK
    },
    "1":{
        SHIFT:{"value" : "!"},
        VOID:{"value" : "1"},
        "key_mask":DEFAULT_MASK
    },
    "2":{
        SHIFT:{"value" : "\""},
        VOID:{"value" : "2"},
        "key_mask":DEFAULT_MASK
    },
    "3":{
        SHIFT:{"value" : "£"},
        VOID:{"value" : "3"},
        "key_mask":DEFAULT_MASK
    },
    "4":{
        SHIFT:{"value" : "$"},
        VOID:{"value" : "4"},
        "key_mask":DEFAULT_MASK
    },
    "5":{
        SHIFT:{"value" : "%"},
        VOID:{"value" : "5"},
        "key_mask":DEFAULT_MASK
    },
    "6":{
        SHIFT:{"value" : "^"},
        VOID:{"value" : "6"},
        "key_mask":DEFAULT_MASK
    },
    "7":{
        SHIFT:{"value" : "&"},
        VOID:{"value" : "7"},
        "key_mask":DEFAULT_MASK
    },
    "8":{
        SHIFT:{"value" : "*"},
        VOID:{"value" : "8"},
        "key_mask":DEFAULT_MASK
    },
    "9":{
        SHIFT:{"value" : "("},
        VOID:{"value" : "9"},
        "key_mask":DEFAULT_MASK
    },
    "0":{
        SHIFT:{"value" : ")"},
        VOID:{"value" : "0"},
        "key_mask":DEFAULT_MASK
    },
    "-":{
        SHIFT:{"value" : "_"},
        VOID:{"value" : "-"},
        "key_mask":DEFAULT_MASK
    },
    "=":{
        SHIFT:{"value" : "+"},
        VOID:{"value" : "="},
        "key_mask":DEFAULT_MASK
    },
    "\\":{
        SHIFT:{"value" : "|"},
        VOID:{"value" : "\\"},
        "key_mask":DEFAULT_MASK
    },

    "tab":{
        VOID:{"value" : Key.tab},
        "key_mask":NO_MOD_MASK
    },
    "q":{
        SHIFT:{"value" : "Q"},
        VOID:{"value" : "q"},
        "key_mask":DEFAULT_MASK
    },
    "w":{
        SHIFT:{"value" : "W"},
        VOID:{"value" : "w"},
        "key_mask":DEFAULT_MASK
    },
    "e":{
        SHIFT:{"value" : "E"},
        VOID:{"value" : "e"},
        ALT:{"value" : "€"},
        "key_mask":DEFAULT_MASK
    },
    "r":{
        SHIFT:{"value" : "R"},
        VOID:{"value" : "r"},
        "key_mask":DEFAULT_MASK
    },
    "t":{
        SHIFT:{"value" : "T"},
        VOID:{"value" : "t"},
        "key_mask":DEFAULT_MASK
    },
    "y":{
        SHIFT:{"value" : "Y"},
        VOID:{"value" : "y"},
        "key_mask":DEFAULT_MASK
    },
    "u":{
        SHIFT:{"value" : "U"},
        VOID:{"value" : "u"},
        "key_mask":DEFAULT_MASK
    },
    "i":{
        SHIFT:{"value" : "I"},
        VOID:{"value" : "i"},
        "key_mask":DEFAULT_MASK
    },
    "o":{
        SHIFT:{"value" : "O"},
        VOID:{"value" : "o"},
        "key_mask":DEFAULT_MASK
    },
    "p":{
        SHIFT:{"value" : "P"},
        VOID:{"value" : "p"},
        "key_mask":DEFAULT_MASK
    },
    "[":{
        SHIFT:{"value" : "{"},
        VOID:{"value" : "["},
        "key_mask":DEFAULT_MASK
    },
    "]":{
        SHIFT:{"value" : "}"},
        VOID:{"value" : "]"},
        "key_mask":DEFAULT_MASK
    },
    "a":{
        SHIFT:{"value" : "A"},
        VOID:{"value" : "a"},
        "key_mask":DEFAULT_MASK
    },
    "s":{
        SHIFT:{"value" : "S"},
        VOID:{"value" : "s"},
        "key_mask":DEFAULT_MASK
    },
    "d":{
        SHIFT:{"value" : "D"},
        VOID:{"value" : "d"},
        "key_mask":DEFAULT_MASK
    },
    "f":{
        SHIFT:{"value" : "F"},
        VOID:{"value" : "f"},
        "key_mask":DEFAULT_MASK
    },
    "g":{
        SHIFT:{"value" : "G"},
        VOID:{"value" : "g"},
        "key_mask":DEFAULT_MASK
    },
    "h":{
        SHIFT:{"value" : "H"},
        VOID:{"value" : "h"},
        "key_mask":DEFAULT_MASK
    },
    "j":{
        SHIFT:{"value" : "J"},
        VOID:{"value" : "j"},
        "key_mask":DEFAULT_MASK
    },
    "k":{
        SHIFT:{"value" : "K"},
        VOID:{"value" : "k"},
        "key_mask":DEFAULT_MASK
    },
    "l":{
        SHIFT:{"value" : "L"},
        VOID:{"value" : "l"},
        "key_mask":DEFAULT_MASK
    },
    ";":{
        SHIFT:{"value" : ":"},
        VOID:{"value" : ";"},
        "key_mask":DEFAULT_MASK
    },
    "#":{
        SHIFT:{"value" : "@"},
        VOID:{"value" : "#"},
        "key_mask":DEFAULT_MASK
    },
    "z":{
        SHIFT:{"value" : "Z"},
        VOID:{"value" : "z"},
        "key_mask":DEFAULT_MASK
    },
    "x":{
        SHIFT:{"value" : "X"},
        VOID:{"value" : "x"},
        "key_mask":DEFAULT_MASK
    },
    "c":{
        SHIFT:{"value" : "C"},
        VOID:{"value" : "c"},
        "key_mask":DEFAULT_MASK
    },
    "v":{
        SHIFT:{"value" : "V"},
        VOID:{"value" : "v"},
        "key_mask":DEFAULT_MASK
    },
    "b":{
        SHIFT:{"value" : "B"},
        VOID:{"value" : "b"},
        "key_mask":DEFAULT_MASK
    },
    "n":{
        SHIFT:{"value" : "N"},
        VOID:{"value" : "n"},
        "key_mask":DEFAULT_MASK
    },
    "m":{
        SHIFT:{"value" : "M"},
        VOID:{"value" : "m"},
        "key_mask":DEFAULT_MASK
    },
    ",":{
        SHIFT:{"value" : "<"},
        VOID:{"value" : ","},
        "key_mask":DEFAULT_MASK
    },
    ".":{
        SHIFT:{"value" : ">"},
        VOID:{"value" : "."},
        "key_mask":DEFAULT_MASK
    },
    "/":{
        SHIFT:{"value" : "?"},
        VOID:{"value" : "/"},
        "key_mask":DEFAULT_MASK
    },
    "shift_right": {
        VOID : {"value" : Key.shift_r},
        "key_mask":NO_MOD_MASK
    },
    "shift_left": {
        VOID : {"value" : Key.shift_l},
        "key_mask":NO_MOD_MASK
    },
    "ctrl": {
        VOID : {"value" : Key.ctrl_l},
        "key_mask":NO_MOD_MASK
    },
    "alt_right": {
        VOID : {"value" : Key.alt},
        "key_mask":NO_MOD_MASK
    },
    "alt_left": {
        VOID : {"value" : Key.alt},
        "key_mask":NO_MOD_MASK
    },
    "amiga_left": {
        VOID : {"value" : Key.cmd_l},
        "key_mask":NO_MOD_MASK
    },
    "amiga_right": {
        VOID : {"value" : Key.cmd_r},
        "key_mask":NO_MOD_MASK
    },
    "space": {
        VOID : {"value" : " "},
        "key_mask":NO_MOD_MASK
    },
    "up": {
        VOID : {"value" : Key.up},
        "key_mask":NO_MOD_MASK
    },
    "down": {
        VOID : {"value" : Key.down},
        "key_mask":NO_MOD_MASK
    },
    "right": {
        VOID : {"value" : Key.right},
        "key_mask":NO_MOD_MASK
    },
    "left": {
        VOID : {"value" : Key.left},
        "key_mask":NO_MOD_MASK
    },
    "enter": {
        VOID : {"value" : Key.enter},
        "key_mask":NO_MOD_MASK
    },
    "backspace": {
        VOID : {"value" : Key.backspace},
        "key_mask":NO_MOD_MASK
    },
    "del": {
        VOID : {"value" : Key.delete},
        "key_mask":NO_MOD_MASK
    },
    "esc": {
        VOID : {"value" : Key.esc},
        "key_mask":NO_MOD_MASK
    },
    "F1": {
        VOID : {"value" : Key.f1},
        "key_mask":NO_MOD_MASK
    },
    "F2": {
        VOID : {"value" : Key.f2},
        "key_mask":NO_MOD_MASK
    },
    "F3": {
        VOID : {"value" : Key.f3},
        "key_mask":NO_MOD_MASK
    },
    "F4": {
        VOID : {"value" : Key.f4},
        "key_mask":NO_MOD_MASK
    },
    "F5": {
        VOID : {"value" : Key.f5},
        "key_mask":NO_MOD_MASK
    },
    "F6": {
        VOID : {"value" : Key.f6},
        "key_mask":NO_MOD_MASK
    },
    "F7": {
        VOID : {"value" : Key.f7},
        "key_mask":NO_MOD_MASK
    },
    "F8": {
        VOID : {"value" : Key.f8},
        "key_mask":NO_MOD_MASK
    },
    "F9": {
        VOID : {"value" : Key.f9},
        "key_mask":NO_MOD_MASK
    },
    "F10": {
        VOID : {"value" : Key.f10},
        "key_mask":NO_MOD_MASK
    },
    "help": {
        VOID : {"value" : Key.f11},
        "key_mask":NO_MOD_MASK
    },
    "void_right": {
        "key_mask":NO_MOD_MASK
    },
    "void_left": {
        "key_mask":NO_MOD_MASK
    },
    "caps_locks": {
        "key_mask":NO_MOD_MASK
    },
    

}

class SerialInterface:
    def __init__(self, port:str="/dev/ttyACM0", baudrate:int=460800) -> None:
        self._port = port
        self._baudrate = baudrate
        self._serial = None

    def __enter__(self):
        self._serial = serial.Serial(self._port, self._baudrate)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._serial:
            self._serial.close()

    def read_kbn_frame(self)->bytes:
        buffer = []
        while True:
            if len(buffer)  == 0 :
                data = self._serial.read(1)
                if data == b"K":  
                    buffer.append(data)
            elif len(buffer)  == 1 :
                data = self._serial.read(1)
                if data == b"B":  
                    buffer.append(data)
            elif len(buffer)  == 2 :
                data = self._serial.read(1)
                if data == b"N":  
                    buffer.append(data)
            elif len(buffer) == 3 : 
                if buffer != [b"K", b"B", b"N"]:
                    buffer.clear()
                else:
                    size = int.from_bytes(self._serial.read(1), "little")
                    if size > 0:
                        return self._serial.read(size)
                    else:
                        return b""
    def __str__(self):
        return f"{self._port} @ {self._baudrate}"


class SerialKeyboard:
    def __init__(self, serial:SerialInterface, labels=UK_LABELS, keymap=UK_KEYMAP, first_repeat:int=100, other_repeat:int=30):
        self._serial = serial
        self._keyboard = Controller()

        self._labels = labels
        self._keymap = keymap
        self._first_repeat = first_repeat
        self._other_repeat = other_repeat

        self._modifiers = VOID
        self._applied_keymap = {}
        self._pressed_keys = {}
        self._log = logging.getLogger("SerialKeyboard")
                   
    def do(self):
        while True:
            try:
                with self._serial as s:
                    keys = s.read_kbn_frame()
            except serial.serialutil.SerialException as e:
                time.sleep(1)
                self._log.error(f"can't connect to Serial port {self._serial}")
                continue
            
            keys = [self._labels [k] for k in keys]
            for key in keys:
                if key not in self._pressed_keys:
                    self._pressed_keys[key] = 0
                    self._log.debug(f"Raw keycode {key} hit")
                else:
                    self._pressed_keys[key] += 1

            released_keys = set(self._pressed_keys.keys()) - set(keys)

            if len(released_keys) > 0:
                self._log.debug(f"Raw keycode {key} release")
            for release_key in released_keys:
                del self._pressed_keys[release_key]

            self.set_modifiers()

            self.apply_keymap(released_keys)

    def set_modifiers(self):
        self._modifiers = self._modifiers & CAPS_LOCKS

        if "alt_right" in self._pressed_keys or "alt_left" in self._pressed_keys:
            self._modifiers |= ALT

        if "ctrl" in self._pressed_keys:
            self._modifiers |= CTRL

        if "amiga_right" in self._pressed_keys:
            self._modifiers |= AMIGA_RIGHT

        if "amiga_left" in self._pressed_keys:
            self._modifiers |= AMIGA_LEFT

        if "caps_locks" in self._pressed_keys:
            if self._pressed_keys["caps_locks"] == 0:
                self._modifiers ^= CAPS_LOCKS

        if ("shift_right" in self._pressed_keys or "shift_left" in self._pressed_keys) ^ (self._modifiers & CAPS_LOCKS == CAPS_LOCKS):
            self._modifiers |= SHIFT

    def apply_keymap(self, released_keys:set):
        for labeled_key in self._pressed_keys:
            mask = self._modifiers & self._keymap[labeled_key]["key_mask"]
            conf = self._keymap[labeled_key].get(mask, {})

            if "value" in conf:
                real_key = conf["value"]
                if labeled_key in self._applied_keymap and self._applied_keymap[labeled_key] != real_key:
                    self._pressed_keys[labeled_key] = 0
                    self._keyboard.release(self._applied_keymap[labeled_key])
                    self._log.debug(f"Key {labeled_key} release")
                    del self._applied_keymap[labeled_key]

                if self._pressed_keys[labeled_key] == 0:
                    self._applied_keymap[labeled_key] = real_key
                    self._keyboard.press(real_key)
                    self._log.debug(f"Key {real_key} hit")
                if self._pressed_keys[labeled_key] > (self._first_repeat + self._other_repeat):
                    self._keyboard.press(real_key)
                    self._pressed_keys[labeled_key] = self._first_repeat

        for labeled_key in released_keys:
            if labeled_key in self._applied_keymap:
                self._keyboard.release(self._applied_keymap[labeled_key])
                self._log.debug(f"Key {labeled_key} release")
                del self._applied_keymap[labeled_key]
            

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    serial_interface = SerialInterface()
    serial_keyboard = SerialKeyboard(serial_interface)
    try:
        serial_keyboard.do()            

    except KeyboardInterrupt:
        pass
