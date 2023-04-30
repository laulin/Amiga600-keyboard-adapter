import serial
from pynput.keyboard import Controller
from pynput.keyboard import Key


arduino_port = "/dev/ttyACM0"
arduino_baudrate = 460800

ser = serial.Serial(arduino_port, arduino_baudrate)
keyboard = Controller()

pressed_keys = {}
released_keys = set()

LABELS = {
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

modifiers = VOID

modifier_masks = {
    "shift" : SHIFT,
    "alt" : ALT,
    "amiga_right" : AMIGA_RIGHT,
    "amiga_left" : AMIGA_LEFT,
    "ctrl" : CTRL,
    "caps_locks" : CAPS_LOCKS
}

keymap = {
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
    

}

def set_modifiers():
    global modifiers
    modifiers = modifiers & CAPS_LOCKS

    if "alt_right" in pressed_keys or "alt_left" in pressed_keys:
        modifiers |= ALT

    if "ctrl" in pressed_keys:
        modifiers |= CTRL

    if "amiga_right" in pressed_keys:
        modifiers |= AMIGA_RIGHT

    if "amiga_left" in pressed_keys:
        modifiers |= AMIGA_LEFT

    if "caps_locks" in pressed_keys:
        if pressed_keys["caps_locks"] == 0:
            modifiers ^= CAPS_LOCKS

    if ("shift_right" in pressed_keys or "shift_left" in pressed_keys) ^ (modifiers & CAPS_LOCKS == CAPS_LOCKS):
        modifiers |= SHIFT


def read_kbn_frame(ser:serial.Serial)->bytes:
    """
    This function reads a frame of data from a serial port that starts with the characters "KBN" and
    returns the data payload of the frame.
    
    :param ser: The parameter "ser" is a serial.Serial object, which is an instance of the Serial class
    from the PySerial library. It represents a serial port connection and is used to read and write data
    to and from the port
    :type ser: serial.Serial
    :return: a bytes object, which is the data received from the serial port after successfully reading
    a KBN frame.
    """
    buffer = []
    while True:
        if len(buffer)  == 0 :
            data = ser.read(1)
            if data == b"K":  
                buffer.append(data)
        elif len(buffer)  == 1 :
            data = ser.read(1)
            if data == b"B":  
                buffer.append(data)
        elif len(buffer)  == 2 :
            data = ser.read(1)
            if data == b"N":  
                buffer.append(data)
        elif len(buffer) == 3 : 
            if buffer != [b"K", b"B", b"N"]:
                buffer.clear()
            else:
                size = int.from_bytes(ser.read(1), "little")
                if size > 0:
                    return ser.read(size)
                else:
                    return b""

applied_keymap = {}

def get_key_configuration(labeled_key, mask):
    return keymap[labeled_key].get(mask, {})

def apply_keymap():
    for labeled_key in pressed_keys:
        mask = modifiers & keymap[labeled_key]["key_mask"]
        conf = get_key_configuration(labeled_key, mask)

        if "value" in conf:
            real_key = conf["value"]
            if labeled_key in applied_keymap and applied_keymap[labeled_key] != real_key:
                pressed_keys[labeled_key] = 0
                keyboard.release(applied_keymap[labeled_key])
                del applied_keymap[labeled_key]

            if pressed_keys[labeled_key] == 0:
                applied_keymap[labeled_key] = real_key
                keyboard.press(real_key)
                #print(f"press {labeled_key} ({real_key})")
            if pressed_keys[labeled_key] > 30:
                keyboard.press(real_key)
                pressed_keys[labeled_key] = 25
                #print(f"press {labeled_key} ({real_key})")

    for labeled_key in released_keys:
        if labeled_key in applied_keymap:
            keyboard.release(applied_keymap[labeled_key])
            del applied_keymap[labeled_key]


try:
    while True:
        keys = read_kbn_frame(ser)
        keys = [LABELS[k] for k in keys]
        for key in keys:
            if key not in pressed_keys:
                pressed_keys[key] = 0
            else:
                pressed_keys[key] += 1

        released_keys = set(pressed_keys.keys()) - set(keys)

        for release_key in released_keys:
            del pressed_keys[release_key]

        # if len(pressed_keys) > 0:
        #     print(pressed_keys)
        set_modifiers()
        # if any(modifiers.values()):
        #     print(modifiers)

        apply_keymap()
        

except KeyboardInterrupt:
    ser.close()
