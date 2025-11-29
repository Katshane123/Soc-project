# Encryption program 

import random 
import string

chars = " "+ string.punctuation +  string.digits + string.ascii_letters 
chars = list(chars)# Type cast the individual chars into a List [g,p,k,o]
key = chars.copy() #Encryption key

random.shuffle(key) #This will shuffle the key list so it doesnt match Char list

#Encryption 

plain_text = input('Enter a message to encrypt: ')
cipher_text =""

for letter in plain_text:
    index = chars.index(letter) #locate the index of the letter in plain text
    cipher_text = cipher_text + key[index] #Match the Ptxt index to key index, add to cipher string

print(f'Original message : {plain_text} ')
print(f'Encrypted message : {cipher_text}')

#Decryption

cipher_text = input('Enter a message to decrypt: ')
plain_text  =" "

for letter in cipher_text:
    index = key.index(letter)
    plain_text= plain_text + chars[index]

print(f'Encrypted message: {cipher_text} ')
print(f'Original message : {plain_text}')