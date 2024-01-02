from cryptography.fernet import Fernet

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