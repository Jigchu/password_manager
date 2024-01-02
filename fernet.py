from cryptography.fernet import Fernet

import data

fernet_key: bytes = data.retrieve_key()
fernet: Fernet = Fernet(key=fernet_key)