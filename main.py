import secrets
import string
import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate secure random passwords.")
    parser.add_argument("--length", type=int, default=16, help="password length (default: 16)")
    parser.add_argument("--no-uppercase", action="store_true", help="exclude A-Z")
    parser.add_argument("--no-lowercase", action="store_true", help="exclude a-z")
    parser.add_argument("--no-digits", action="store_true", help="exclude 0-9")
    parser.add_argument("--no-symbols", action="store_true", help="exclude symbols")
    parser.add_argument("--count", type=int, default=1, help="number of passwords (default: 1)")
    
    # simpan hasil parsing dulu, jangan langsung return
    args = parser.parse_args()
    
    if args.length <= 0:
        parser.error("--length must be a positive integer")
        
    if args.count <= 0:
        parser.error("--count must be a positive integer")
        
    # Kalau semua kategori dimatikan, charset akan kosong → tidak ada karakter untuk dipilih
    if args.no_lowercase and args.no_uppercase and args.no_digits and args.no_symbols:
        parser.error("at least one character set must be enabled")

                
    return args
    
def build_charset(lowercase: bool, uppercase: bool, digits: bool, symbols: bool) -> str: 
        # Mulai dari string kosong, tambahkan kategori yang aktif saja
        charset: str = ""
        if lowercase:
            charset += string.ascii_lowercase
        if uppercase:
            charset += string.ascii_uppercase
        if digits:
            charset += string.digits
        if symbols:
            charset += string.punctuation
        return charset
    
def generate(length: int, charset: str) ->str:
    # Pilih karakter acak dari charset sebanyak 'length' kali memakai CSPRNG
    random_string: str = ''.join(secrets.choice(charset) for _ in range(length))
    return random_string

def main() -> None:
    args = parse_args()
    
    charset = build_charset(
        lowercase=not args.no_lowercase,
        uppercase=not args.no_uppercase,
        digits=not args.no_digits,
        symbols=not args.no_symbols
    )

    for _ in range(args.count):
        print(generate(args.length, charset))

        
if __name__ == "__main__":
    main()