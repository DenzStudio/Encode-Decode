import base64
import os

def encode_base64(text):
    encoded = base64.b64encode(text.encode()).decode()
    return encoded

def save_to_file(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"[+] Hasil disimpan ke {filename}")
    except Exception as e:
        print(f"[!] Gagal menyimpan file: {e}")

def main():
    print("🔐 Base64 Encoder Tool by DenzzCoder Team")
    print("1. Encode teks langsung")
    print("2. Encode isi file")
    
    choice = input("Pilih opsi (1/2): ")

    if choice == "1":
        text_input = input("Masukkan teks yang ingin di-encode: ")
    elif choice == "2":
        file_path = input("Masukkan path file: ").strip()
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text_input = f.read()
        except Exception as e:
            print(f"[!] Gagal membaca file: {e}")
            return
    else:
        print("[!] Pilihan tidak valid.")
        return

    encoded_text = encode_base64(text_input)
    print("\n🔒 Hasil Base64:")
    print(encoded_text)

    save = input("\nSimpan hasil ke file? (y/n): ").lower() == 'y'
    if save:
        output_file = input("Masukkan nama file output: ")
        save_to_file(encoded_text, output_file)

if __name__ == "__main__":
    main()