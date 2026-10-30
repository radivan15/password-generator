import secrets
import string

def generate(length: int) ->str:
    # Charset: semua huruf kecil a-z, disediakan oleh modul string
    charset: str = string.ascii_lowercase

    # Pilih karakter acak dari charset sebanyak 'length' kali memakai CSPRNG
    random_string: str = ''.join(secrets.choice(charset) for _ in range(length))
    return random_string

def main() -> None:
    password = generate(16)
    print(password)
    print("password length:", len(password))
    
    
if __name__ == "__main__":
    main()