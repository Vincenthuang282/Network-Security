### XOR  Decipher
### Training 1.1.a: Having a ciphertext and a key and to decrypt the ciphertext.
### Encryption (XOR with Key): Ciphertext = Plaintext ^ Key
### Decryption (XOR with Key): Plaintext = Ciphertext ^ Key


def xor_decrpt(ciphertext, keytext):
    decrypted_text=bytearray()
    len_of_text=len(keytext)

    for i in range(len_of_text):
        decrypted_bit=ciphertext[i] ^ keytext[i]
        decrypted_text.append(decrypted_bit)
    return decrypted_text


ciphertext_file_path="C:/Users/VINCENT/OneDrive/桌面/Advanced Network Security/1/forstudents/a/ciphertext.bin"
key_file_path="C:/Users/VINCENT/OneDrive/桌面/Advanced Network Security/1/forstudents/a/key.bin"

with open(ciphertext_file_path, 'rb') as file:
    ciphertext=file.read()
with open(key_file_path, "rb") as file:
    keytext=file.read()
decrypted_text= xor_decrpt(ciphertext,keytext) 
print(decrypted_text.decode("utf-8"))