import secrets
import string


def main() -> None:
    # Charset: semua huruf kecil a-z, disediakan oleh modul string
    charset: str = ""

    # Pilih 1 karakter acak dari charset memakai CSPRNG
    char: str = secrets.choice(charset)
    print(char)
    
if __name__ == "__main__":
    main()