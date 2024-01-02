from cryptography.fernet import Fernet

import key

fernet_key: bytes = key.retrieve_key()
fernet: Fernet = Fernet(key=fernet_key)