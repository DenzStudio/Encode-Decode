import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def crack_sha256(target_hash, max_length=6):
    chars = "abcdefghijklmnopqrstuvwxyz"
    for length in range(1, max_length+1):
        print(f"[+] Mencoba panjang {length}...")
        for i in range(len(chars)**length):
            word = ""
            idx = i
            for _ in range(length):
                idx, ch = divmod(idx, len(chars))
                word = chars[ch] + word
            if sha256_hash(word) == target_hash:
                print(f"[✅] Berhasil! Teks asli: {word}")
                return word
    print("[-] Tidak ditemukan.")
    return None

# Ganti dengan hash yang ingin kamu coba
target_hash = "13077bd8f9ee0156e1e972f62402d5f4a64d642dabc50a6df8e787aedb5678e1"

crack_sha256(target_hash, max_length=8)