
#include "keymap.h"
#include <Arduino.h>
#include <Keyboard.h>

const uint8_t KEYMAP[256] = {
    0 , // 0x0 : 
    0 , // 0x1 : 
    0 , // 0x2 : 
    0 , // 0x3 : 
    0 , // 0x4 : 
    0 , // 0x5 : 
    0 , // 0x6 : 
    0 , // 0x7 : 
    0 , // 0x8 : 
    0 , // 0x9 : 
    0 , // 0xa : 
    0 , // 0xb : 
    0 , // 0xc : 
    0 , // 0xd : 
    0 , // 0xe : 
    0 , // 0xf : 
    KEY_LEFT_ALT , // 0x10 : alt left
    0 , // 0x11 : 
    0 , // 0x12 : 
    0 , // 0x13 : 
    0 , // 0x14 : 
    0 , // 0x15 : 
    0 , // 0x16 : 
    0 , // 0x17 : 
    0 , // 0x18 : 
    0 , // 0x19 : 
    0 , // 0x1a : 
    0 , // 0x1b : 
    0 , // 0x1c : 
    0 , // 0x1d : 
    0 , // 0x1e : 
    0 , // 0x1f : 
    KEY_LEFT_SHIFT , // 0x20 : shift left
    0 , // 0x21 : 
    0 , // 0x22 : 
    0 , // 0x23 : 
    0 , // 0x24 : 
    0 , // 0x25 : 
    0 , // 0x26 : 
    0 , // 0x27 : 
    0 , // 0x28 : 
    0 , // 0x29 : 
    0 , // 0x2a : 
    0 , // 0x2b : 
    0 , // 0x2c : 
    0 , // 0x2d : 
    0 , // 0x2e : 
    0 , // 0x2f : 
    KEY_LEFT_CTRL , // 0x30 : ctrl
    0 , // 0x31 : 
    0 , // 0x32 : 
    0 , // 0x33 : 
    0 , // 0x34 : 
    0 , // 0x35 : 
    0 , // 0x36 : 
    0 , // 0x37 : 
    0 , // 0x38 : 
    0 , // 0x39 : 
    0 , // 0x3a : 
    0 , // 0x3b : 
    0 , // 0x3c : 
    0 , // 0x3d : 
    0 , // 0x3e : 
    0 , // 0x3f : 
    0 , // 0x40 : 
    0 , // 0x41 : 
    0 , // 0x42 : 
    0 , // 0x43 : 
    0 , // 0x44 : 
    0 , // 0x45 : 
    0 , // 0x46 : 
    0 , // 0x47 : 
    0 , // 0x48 : 
    0 , // 0x49 : 
    0 , // 0x4a : 
    0 , // 0x4b : 
    0 , // 0x4c : 
    0 , // 0x4d : 
    0 , // 0x4e : 
    0 , // 0x4f : 
    0 , // 0x50 : 
    0 , // 0x51 : 
    0 , // 0x52 : 
    0 , // 0x53 : 
    0 , // 0x54 : 
    0 , // 0x55 : 
    0 , // 0x56 : 
    0 , // 0x57 : 
    0 , // 0x58 : 
    0 , // 0x59 : 
    0 , // 0x5a : 
    0 , // 0x5b : 
    0 , // 0x5c : 
    0 , // 0x5d : 
    0 , // 0x5e : 
    0 , // 0x5f : 
    KEY_RIGHT_ALT , // 0x60 : alt right
    0 , // 0x61 : 
    0 , // 0x62 : 
    0 , // 0x63 : 
    0 , // 0x64 : 
    0 , // 0x65 : 
    0 , // 0x66 : 
    0 , // 0x67 : 
    0 , // 0x68 : 
    0 , // 0x69 : 
    0 , // 0x6a : 
    0 , // 0x6b : 
    0 , // 0x6c : 
    0 , // 0x6d : 
    0 , // 0x6e : 
    0 , // 0x6f : 
    0 , // 0x70 : 
    KEY_DOWN_ARROW , // 0x71 : down arrow
    KEY_BACKSPACE , // 0x72 : backspace
    0x20 , // 0x73 : space
    0 , // 0x74 : 
    ',' , // 0x75 : ?
    '>' , // 0x76 : >
    '<' , // 0x77 : <
    0x59 , // 0x78 : m
    'n' , // 0x79 : n
    'b' , // 0x7a : b
    'v' , // 0x7b : v
    'c' , // 0x7c : c
    'x' , // 0x7d : x
    'z' , // 0x7e : z
    '<' , // 0x7f : void left
    KEY_RIGHT_SHIFT , // 0x80 : shift right
    0 , // 0x81 : 
    0 , // 0x82 : 
    0 , // 0x83 : 
    0 , // 0x84 : 
    0 , // 0x85 : 
    0 , // 0x86 : 
    0 , // 0x87 : 
    0 , // 0x88 : 
    0 , // 0x89 : 
    0 , // 0x8a : 
    0 , // 0x8b : 
    0 , // 0x8c : 
    0 , // 0x8d : 
    0 , // 0x8e : 
    0 , // 0x8f : 
    0 , // 0x90 : 
    KEY_RIGHT_ARROW , // 0x91 : right arrow
    KEY_DELETE , // 0x92 : del
    0 , // 0x93 : 
    '*' , // 0x94 : @
    0x59 , // 0x95 : :
    'l' , // 0x96 : l
    'k' , // 0x97 : k
    'j' , // 0x98 : j
    'h' , // 0x99 : h
    'g' , // 0x9a : g
    'f' , // 0x9b : f
    'd' , // 0x9c : d
    's' , // 0x9d : s
    'a' , // 0x9e : a
    KEY_CAPS_LOCK , // 0x9f : caps locks
    0 , // 0xa0 : 
    0 , // 0xa1 : 
    0 , // 0xa2 : 
    0 , // 0xa3 : 
    0 , // 0xa4 : 
    0 , // 0xa5 : 
    0 , // 0xa6 : 
    0 , // 0xa7 : 
    0 , // 0xa8 : 
    0 , // 0xa9 : 
    0 , // 0xaa : 
    0 , // 0xab : 
    0 , // 0xac : 
    0 , // 0xad : 
    0 , // 0xae : 
    0 , // 0xaf : 
    0 , // 0xb0 : 
    KEY_LEFT_ARROW , // 0xb1 : left arrow
    KEY_RETURN , // 0xb2 : enter
    ']' , // 0xb3 : }
    '[' , // 0xb4 : {
    'p' , // 0xb5 : p
    'o' , // 0xb6 : o
    'i' , // 0xb7 : i
    'u' , // 0xb8 : u
    'y' , // 0xb9 : y
    't' , // 0xba : t
    'r' , // 0xbb : r
    'e' , // 0xbc : e
    'z' , // 0xbd : w
    'q' , // 0xbe : q
    KEY_TAB , // 0xbf : tab
    0 , // 0xc0 : 
    KEY_UP_ARROW , // 0xc1 : arrow up
    '\\' , // 0xc2 : |
    '=' , // 0xc3 : +
    '-' , // 0xc4 : _
    '0' , // 0xc5 : )
    '9' , // 0xc6 : (
    '8' , // 0xc7 : *
    '7' , // 0xc8 : &
    '6' , // 0xc9 : ^
    '5' , // 0xca : %
    '4' , // 0xcb : £
    '3' , // 0xcc : £
    '2' , // 0xcd : '"'
    '1' , // 0xce : !
    '`' , // 0xcf : tild
    0 , // 0xd0 : 
    0 , // 0xd1 : 
    KEY_F10 , // 0xd2 : F10
    KEY_F9 , // 0xd3 : F9
    KEY_F8 , // 0xd4 : F8
    KEY_F7 , // 0xd5 : F7
    0 , // 0xd6 : 
    KEY_F6 , // 0xd7 : F6
    0 , // 0xd8 : 
    KEY_F5 , // 0xd9 : F5
    KEY_F4 , // 0xda : F4
    KEY_F3 , // 0xdb : F3
    KEY_F2 , // 0xdc : F2
    KEY_F1 , // 0xdd : F1
    0 , // 0xde : 
    KEY_ESC , // 0xdf : esc
    0 , // 0xe0 : 
    0 , // 0xe1 : 
    0 , // 0xe2 : 
    0 , // 0xe3 : 
    0 , // 0xe4 : 
    0 , // 0xe5 : 
    0 , // 0xe6 : 
    0 , // 0xe7 : 
    0 , // 0xe8 : 
    0 , // 0xe9 : 
    0 , // 0xea : 
    0 , // 0xeb : 
    0 , // 0xec : 
    0 , // 0xed : 
    0 , // 0xee : 
    0 , // 0xef : 
    0 , // 0xf0 : 
    0 , // 0xf1 : 
    0 , // 0xf2 : 
    0 , // 0xf3 : 
    0 , // 0xf4 : 
    0 , // 0xf5 : 
    0 , // 0xf6 : 
    0 , // 0xf7 : 
    0 , // 0xf8 : 
    0 , // 0xf9 : 
    0 , // 0xfa : 
    0 , // 0xfb : 
    0 , // 0xfc : 
    0 , // 0xfd : 
    0 , // 0xfe : 
    0 , // 0xff : 
};

