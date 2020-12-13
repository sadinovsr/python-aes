import os, argparse, AES
from Crypto.Random import get_random_bytes

ivs = 'ivs/'
docs = '../documents/'

def genKey():
	key = get_random_bytes(16)
	with open("key.key", "wb") as file:
			file.write(key)

# -----------------------------------------

def encrypt(filename, key):
	with open(docs + filename, "rb") as file:
		fileData = file.read()

	iv = get_random_bytes(16)

	result = AES.AES(key).encryptCBC(fileData, iv)

	with open(ivs + filename + '.iv.key', 'wb') as file:
		file.write(iv)

	with open(docs + filename + '.enc', "wb") as file:
		file.write(result)

	os.remove(docs + filename)


def decrypt(filename, key):
	with open(docs + filename + '.enc', "rb") as file:
		fileData = file.read()

	with open(ivs + filename + '.iv.key', "rb") as file:
		iv = file.read()

	decrypted = AES.AES(key).decryptCBC(fileData, iv)

	with open(docs + filename, "wb") as file:
		file.write(decrypted)

	os.remove(docs + filename + '.enc')
	os.remove(ivs + filename + '.iv.key')

# -----------------------------------------

parser = argparse.ArgumentParser(description="Simple File Encryptor Script")
parser.add_argument("filename", help="File to encrypt/decrypt")
parser.add_argument("-g", "--generate-key", dest="generateKey", action="store_true",
										help="generate a new key which overwrites previous one if it exists")
parser.add_argument("-e", "--encrypt", action="store_true",
										help="encrypt the file, only -e or -d can be specified.")
parser.add_argument("-d", "--decrypt", action="store_true",
										help="decrypt the file, only -e or -d can be specified.")

args = parser.parse_args()
filename = args.filename
generateKey = args.generateKey

if generateKey:
		genKey()
		
with open("key.key", "rb") as file:
			key = file.read()

if len(key) != 16:
	raise TypeError("Not valid key. Please add -g argument to generate and store it.")

encryptChosen = args.encrypt
decryptChosen = args.decrypt

if encryptChosen and decryptChosen:
		raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
elif encryptChosen:
		encrypt(filename, key)
elif decryptChosen:
		decrypt(filename, key)
else:
		raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")