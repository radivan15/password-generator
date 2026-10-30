import secrets
import string
import argparse

def parse_args() -> argparse.Namespace:
    # parseer = membaca args dari command line
    parser = argparse.ArgumentParser(description="Generate secure random passwords.")
    # daftarkan flag --length dengan tipe int, default 16
    parser.add_argument("--length", type=int, default=16, help="password length (default: 16)")
    return parser.parse_args()
    
def generate(length: int) ->str:
    # Charset: semua huruf kecil a-z, disediakan oleh modul string
    charset: str = string.ascii_lowercase

    # Pilih karakter acak dari charset sebanyak 'length' kali memakai CSPRNG
    random_string: str = ''.join(secrets.choice(charset) for _ in range(length))
    return random_string

def main() -> None:
    args = parse_args()
    password = generate(args.length)
    print(password)

    
    
if __name__ == "__main__":
    main()