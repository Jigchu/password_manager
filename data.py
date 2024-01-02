from cryptography.fernet import Fernet

from fernet import fernet

# Retrieves fernet key, creates one if not
def retrieve_key():
	key: bytes = b""

	try:
		with open("storage.key", mode="rb") as fernet_key:
			pass
	except FileNotFoundError:
		with open("storage.key", mode="xb") as fernet_key:
			new_key = Fernet.generate_key()
			fernet_key.write(new_key)
	
	with open("storage.key", mode="rb") as fernet_key:
		key = fernet_key.read()
	
	return key

def decrypt_data():
	try:
		with open("storage.txt", mode="rb") as encrypted_data:
			pass
	except FileNotFoundError:
		with open("storage.txt", mode="xb") as encrypted_data:
			return b""
	
	with open("storage.txt", mode="rb") as encrypted_data:
		data = encrypted_data.read().strip()
		data = fernet.decrypt(data)
		
	return data

def retrive_data():
	byte_data: bytes = decrypt_data()
	data: str = byte_data.decode(encoding="utf-8")
	data = data.strip()
	passwords = {}
	for i, s in enumerate(data):
		if i % 2 == 0:
			passwords[s] = data[i+1]

	return passwords