import serial
from pynput.keyboard import Controller


arduino_port = "/dev/ttyACM0"
arduino_baudrate = 115200

ser = serial.Serial(arduino_port, arduino_baudrate)
keyboard = Controller()

activated_keys = {}

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

def set_modifiers():
    modifiers["shift"] = False
    modifiers["alt"] = False
    modifiers["ctrl"] = False
    modifiers["amiga_right"] = False
    modifiers["amiga_left"] = False

    if "shift_right" in activated_keys or "shift_left" in activated_keys:
        modifiers["shift"] = True

    if "alt_right" in activated_keys or "alt_left" in activated_keys:
        modifiers["alt"] = True

    if "ctrl" in activated_keys:
        modifiers["ctrl"] = True

    if "amiga_right" in activated_keys:
        modifiers["amiga_right"] = True

    if "amiga_left" in activated_keys:
        modifiers["amiga_left"] = True

    if "caps_locks" in activated_keys:
        if activated_keys["caps_locks"] == 0:
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

try:
    while True:
        keys = read_kbn_frame(ser)
        keys = [LABELS[k] for k in keys]
        for key in keys:
            if key not in activated_keys:
                activated_keys[key] = 0
                if key == "q":
                    keyboard.tap("Q")
            else:
                activated_keys[key] += 1

        released_keys = set(activated_keys.keys()) - set(keys)

        for release_key in released_keys:
            del activated_keys[release_key]

        # if len(activated_keys) > 0:
        #     print(activated_keys)
        set_modifiers()
        # if any(modifiers.values()):
        #     print(modifiers)
        

except KeyboardInterrupt:
    ser.close()
