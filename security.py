
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import json
import base64
from typing import Dict, Any

SECRET_KEY = os.getenv("SECRET_KEY", b"1Xt5YfM4ZNuFdwp3OfVkwkhhQLagWKtt1234567890123456")

def encrypt_data(data: Dict[str, Any]) -> str:
    aesgcm = AESGCM(SECRET_KEY)
    nonce = os.urandom(12)
    data_bytes = json.dumps(data).encode()
    ciphertext = aesgcm.encrypt(nonce, data_bytes, None)
    combined = nonce + ciphertext
    return base64.b64encode(combined).decode()

def decrypt_data(encrypted: str) -> Dict[str, Any]:
    aesgcm = AESGCM(SECRET_KEY)
    combined = base64.b64decode(encrypted)
    nonce = combined[:12]
    ciphertext = combined[12:]
    data_bytes = aesgcm.decrypt(nonce, ciphertext, None)
    return json.loads(data_bytes.decode())
