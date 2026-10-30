import secrets
import string
import argparse

def parse_args() -> argparse.Namespace:
    # parseer = membaca args dari command line
    parser = argparse.ArgumentParser(description="Generate secure random passwords.")
    # daftarkan flag --length dengan tipe int, default 16
    parser.add_argument("--length", type=int, default=16, help="password length (default: 16)")
    # Kalau flag dipakai → True, kalau tidak → False. Tidak butuh nilai setelahnya.
    parser.add_argument("--no-uppercase", action="store_true", help="exclude A-Z")
    parser.add_argument("--no-lowercase", action="store_true", help="exclude a-z")
    parser.add_argument("--no-digits", action="store_true", help="exclude 0-9")
    parser.add_argument("--no-symbols", action="store_true", help="exclude symbols")
    return parser.parse_args()
    
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

    password = generate(args.length, charset)
    print(password)

    
    
if __name__ == "__main__":
    main()