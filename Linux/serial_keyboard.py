import serial
from pynput.keyboard import Controller
from pynput.keyboard import Key


arduino_port = "/dev/ttyACM0"
arduino_baudrate = 115200

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
    0xCE : "!",
    0xCD : "\"",
    0xCC : "£",
    0xCA : "%",
    0xC9 : "^",
    0xC8 : "&",
    0xC7 : "*",
    0xC6 : "(",
    0xC5 : ")",
    0xC4 : "_",
    0xC3 : "+",
    0xC2 : "|",
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
    0xB4 : "{",
    0xB3 : "}",
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
    0x95 : ":",
    0x94 : "@",
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
    0x77 : "<",
    0x76 : ">",
    0x75 : "?",
    0x80 : "shift_right",
    0xC1 : "arrow_up",
    0x10 : "alt_left",
    0x00 : "amiga_left",
    0x73 : "space",
    0x40 : "amiga_right",
    0x60 : "alt_right",
    0xB1 : "left_arrow",
    0x71 : "down_arrow",
    0x91 : "right_arrow"
}

modifiers = {
    "shift" : False,
    "alt" : False,
    "amiga_right" : False,
    "amiga_left" : False,
    "ctrl" : False,
    "caps_locks" : False
}

SHIFT = 1
ALT = 2
AMIGA_RIGHT = 4
AMIGA_LEFT = 8
CTRL = 16
CAPS_LOCKS = 32
VOID = 0
IGNORE = -1

modifier_masks = {
    "shift" : SHIFT,
    "alt" : ALT,
    "amiga_right" : AMIGA_RIGHT,
    "amiga_left" : AMIGA_LEFT,
    "ctrl" : CTRL,
    "caps_locks" : CAPS_LOCKS
}

keymap = {
    "q":{
        SHIFT:{"value" : "Q"},
        VOID:{"value" : "q"},
    },
    "e":{
        SHIFT:{"value" : "E"},
        VOID:{"value" : "e"},
        ALT:{"value" : "€"},
    },
    "shift_right": {
        IGNORE : {"value" : Key.shift_r}
    }
}

def set_modifiers():
    modifiers["shift"] = False
    modifiers["alt"] = False
    modifiers["ctrl"] = False
    modifiers["amiga_right"] = False
    modifiers["amiga_left"] = False

    if "shift_right" in pressed_keys or "shift_left" in pressed_keys:
        modifiers["shift"] = True

    if "alt_right" in pressed_keys or "alt_left" in pressed_keys:
        modifiers["alt"] = True

    if "ctrl" in pressed_keys:
        modifiers["ctrl"] = True

    if "amiga_right" in pressed_keys:
        modifiers["amiga_right"] = True

    if "amiga_left" in pressed_keys:
        modifiers["amiga_left"] = True

    if "caps_locks" in pressed_keys:
        if pressed_keys["caps_locks"] == 0:
            modifiers["caps_locks"] = True ^ modifiers["caps_locks"]


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

def make_mask():
    mask = VOID
    for modifier, value in modifiers.items():
        if value:
            mask |= modifier_masks[modifier]
    return mask

def get_key_configuration(labeled_key, mask):
    return keymap.get(labeled_key, {}).get(mask, {})

def apply_keymap():


    for labeled_key in pressed_keys:
        if "value" in get_key_configuration(labeled_key, IGNORE):
            conf = get_key_configuration(labeled_key, IGNORE)
        else:
            mask = make_mask()
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
            if pressed_keys[labeled_key] > 30:
                keyboard.press(real_key)
                pressed_keys[labeled_key] = 25

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
