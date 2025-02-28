import typing as tp
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in plaintext:
        if 'A' <= i <= 'Z':
            ciphertext += chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            ciphertext += chr((ord(i) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += i
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in ciphertext:
        if 'A' <= i <= 'Z':
            plaintext += chr((ord(i) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            plaintext += chr((ord(i) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += i
    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    plaintext = ""
    while plaintext not in dictionary:
        best_shift += 1
        plaintext = decrypt_caesar(ciphertext, best_shift)
    return best_shift

print(encrypt_caesar("PYTHON"))  
print(encrypt_caesar("python"))  
print(encrypt_caesar("Python3.6")) 
print(encrypt_caesar("")) 

print(decrypt_caesar("SBWKRQ"))
print(decrypt_caesar("sbwkrq"))
print(decrypt_caesar("Sbwkrq3.6"))
print(decrypt_caesar(""))

print(caesar_breaker_brute_force("SBWKRQ", {"PYTHON", "python", "Python3.6", "sbwkrq", "Sbwkrq3.6"}))