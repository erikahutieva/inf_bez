from caesar import *

def len_words(plaintext: str, keyword: str)->str:
    word=keyword
    num_word=[]

    while len(word)< len(plaintext):
        word+=keyword

    for i in range(len(plaintext)):
        if 'A' <= word[i] <= 'Z':
            num_word.append(int(ord(word[i])-ord('A')))
        elif 'a' <= word[i] <= 'z':
            num_word.append(int(ord(word[i])-ord('a')))
    return num_word


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    new_word=len_words(plaintext, keyword)
    for i in range(len(plaintext)):
        ciphertext+=encrypt_caesar(plaintext[i], new_word[i])

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:

    plaintext = ""
    new_word=len_words(ciphertext, keyword)
    for i in range(len(ciphertext)):
        plaintext+=decrypt_caesar(ciphertext[i], new_word[i])
    return plaintext

print(encrypt_vigenere("PYTHON", "A"))
print(encrypt_vigenere("python", "a"))
print(encrypt_vigenere("ATTACKATDAWNZ", "LEMON"))
print(decrypt_vigenere("PYTHON", "A"))
print(decrypt_vigenere("python", "a"))
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))