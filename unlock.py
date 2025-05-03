import base64
import re
import os

#Hargai Lah Kreator
def is_base64(s):

    pattern = re.compile(r'^[A-Za-z0-9+/]+={0,2}$')
    if not pattern.match(s):
        return False

    
    if len(s) % 4 != 0:
        return False

    try:
        decoded = base64.b64decode(s).decode('utf-8', errors='ignore')
        return True
    except Exception as e:
        return False


def decode_base64(encoded_str, recursive=False):
    results = []
    current = encoded_str

    while True:
        if not is_base64(current):
            break
        try:
            current = base64.b64decode(current).decode('utf-8')
            results.append(current)
            if not recursive:
                break
        except:
            break

    return results


def read_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"[!] Gagal membaca file: {e}")
        return None


def save_to_file(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"[+] Hasil disimpan ke {filename}")
    except Exception as e:
        print(f"[!] Gagal menyimpan file: {e}")


def main():
    print("🔐 Base64 Decoder Tool by DenzzCoder Team")
    print("1. Decode Base64 dari input langsung")
    print("2. Decode Base64 dari file")
    choice = input("Pilih opsi (1/2): ")

    if choice == "1":
        encoded_input = input("Masukkan teks Base64: ").strip()
    elif choice == "2":
        file_path = input("Masukkan path file: ").strip()
        encoded_input = read_from_file(file_path)
        if not encoded_input:
            return
    else:
        print("[!] Pilihan tidak valid.")
        return

    recursive = input("Gunakan mode rekursif? (y/n): ").lower() == 'y'

    if is_base64(encoded_input):
        print("\n[+] Teks terdeteksi sebagai Base64.\n")
        results = decode_base64(encoded_input, recursive=recursive)
        for i, res in enumerate(results):
            print(f"🔄 Level {i+1} → {res}")
        if results:
            save = input("\nSimpan hasil ke file? (y/n): ").lower() == 'y'
            if save:
                output_file = input("Masukkan nama file output: ")
                save_to_file("\n".join(results), output_file)
    else:
        print("[!] Teks bukan Base64 yang valid.")

if __name__ == "__main__":
    main()