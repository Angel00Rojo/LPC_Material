#!/usr/bin/env python3

import base64
from typing import Callable


def encode_decode_bytes(
    byte_message: bytes, encode_fn: Callable[[bytes], bytes]
) -> bytes:
    return encode_fn(byte_message)


def encode_text(text: str, encoding_format: str = "ascii") -> str:
    return encode_decode_bytes(text.encode(encoding_format), base64.b64encode).decode(
        encoding_format
    )


def decode_text(text: str, encoding_format: str = "ascii") -> str:
    return encode_decode_bytes(text.encode(encoding_format), base64.b64decode).decode(
        encoding_format
    )


def encode_file(path: str) -> bytes:
    with open(path, "rb") as file_to_encode:
        return encode_decode_bytes(file_to_encode.read(), base64.b64encode)


def decode_file(path: str) -> bytes:
    file_to_encode = open(path, "rb")
    return encode_decode_bytes(file_to_encode.read(), base64.b64decode)


def save_file(path: str, content: bytes) -> None:
    with open(path, "wb") as file_to_save:
        file_to_save.write(content)


def encode_plus_one(word: str) -> str:
    return "".join([chr(ord(character) + 2) for character in word])


if __name__ == "__main__":
    import sys

    cmds = {"encode": base64.b64encode, "decode": base64.b64decode}
    if len(sys.argv) > 1:
        main_cmd = sys.argv[1]
        encode_format = sys.argv[2] if len(sys.argv) > 2 else "ascii"
        code_function = cmds.get(main_cmd, cmds.get("encode"))
        print(encode_decode_bytes(sys.stdin.read(), code_function))

    #print(encode_plus_one("Hola Mundo"))

    # print(decode_text(encode_text(encode_text('holamundo') + encode_text('valor_llave'))))
    # print((encode_text('any carnal pleasure')))
    #save_file("encoded_hola_mundo.c", encode_file("hola_mundo.c"))
    #print(open("encoded_hola_mundo.c", "rb").read())
    #print(decode_file("encoded_hola_mundo.c"))

    # save_file("decoded_msg.txt", decode_file("encoded_msg.txt"))
    # print(open('decoded_msg.txt', 'rb').read().decode('ascii'))

    #save_file('mystery_img1.txt', encode_file('mystery_img1.png'))
    #print(open('mystery_img1.txt', 'rb').read())
    #save_file('dec_mystery_img2.png', decode_file('mystery_img2.txt'))
