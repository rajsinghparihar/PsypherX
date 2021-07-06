import base64
from Crypto.Cipher import AES

def Enc(password: str, key: str) -> str:
    # converting strings to bytes format to use them in the AES encryption algorithm
    password = bytes(password,'utf-8').rjust(32)
    key = bytes(key.rjust(16),'utf-8')

    # using low security ECB mode of AES since we don't need to be very flashy,
    # this is not used for bank account, it's used for social media and gaming account passwords
    cipher = AES.new(key,AES.MODE_ECB) 
    
    # encoded_bytes variable stores the encoded password in bytes format
    encoded_bytes = base64.b64encode(cipher.encrypt(password))
    
    # we need to convert it to string format, then slice it to make it under 16 characters
    # to satisfy the standard password size limit.
    encoded_pass = str(encoded_bytes)[2:18]
    return encoded_pass