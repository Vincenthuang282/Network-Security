### XOR  Decipher
### Training 1.1.b: Having two ciphertexts and plaintext and to find out the key to decrypt all ciphertexts

def find_key(ciphertext1, plaintext1):
    key=bytearray()
    len_of_the_text=len(ciphertext1)
    for i in range(len_of_the_text):
        decrypted_text=ciphertext1[i] ^ plaintext1[i]
        key.append(decrypted_text)
    return key
def xor_decrpt(ciphertext, keytext):
    decrypted_text=bytearray()
    len_of_text=len(keytext)

    for i in range(len_of_text):
        decrypted_bit=ciphertext[i] ^ keytext[i]
        decrypted_text.append(decrypted_bit)
    return decrypted_text

ciphertext1_file_path="C:/Users/VINCENT/OneDrive/桌面/Advanced Network Security/1/forstudents/b/ciphertext1.bin"
ciphertext2_file_path="C:/Users/VINCENT/OneDrive/桌面/Advanced Network Security/1/forstudents/b/ciphertext2.bin"
plaintext1_file_path="C:/Users/VINCENT/OneDrive/桌面/Advanced Network Security/1/forstudents/b/plaintext1.txt"

with open(ciphertext1_file_path, 'rb') as file:
    ciphertext1=file.read()
with open(ciphertext2_file_path, 'rb') as file:
    ciphertext2=file.read()
with open(plaintext1_file_path, 'rb') as file:
    plaintext1=file.read()

key= find_key(ciphertext1,plaintext1) 
decrypted_text=xor_decrpt(ciphertext2,key) 

print(decrypted_text.decode("utf-8"))
