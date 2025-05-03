import hashlib
import os

def sha256_encode(text):
    # Encode teks menjadi SHA-256 hash
    return hashlib.sha256(text.encode()).hexdigest()

def save_to_file(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"[+] Hasil disimpan ke {filename}")
    except Exception as e:
        print(f"[!] Gagal menyimpan file: {e}")

def main():
    print("🔐 SHA-256 Encoder Tool by DenzzCoder Team")
    text_input = input("Masukkan teks yang ingin di-hash: ")

    hashed_text = sha256_encode(text_input)
    print("\n🔒 Hasil SHA-256 Hash:")
    print(hashed_text)

    save = input("\nSimpan hasil ke file? (y/n): ").lower() == 'y'
    if save:
        output_file = input("Masukkan nama file output: ")
        save_to_file(hashed_text, output_file)

if __name__ == "__main__":
    main()