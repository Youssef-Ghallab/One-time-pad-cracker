def decypher(ciphertexts: list[list[int]]) -> list[list[str]]:
    """
    Deciphers a list of ciphertexts that have been encrypted using the same repeating key.
    
    Args:
        ciphertexts (list[list[int]]): A list of ciphertext byte arrays.
    
    Returns:
        list[list[str]]: A list of deciphered characters for each line.
    """
    length = len(ciphertexts[0])
    cleartexts = [['-' for _ in range(length)] for _ in range(len(ciphertexts))]
    for column in range(length):
        for cipher in ciphertexts:
            if is_space(ciphertexts, cipher, column):
                for i in range(len(cleartexts)):
                    cleartexts[i][column] = chr(cipher[column] ^ ciphertexts[i][column] ^ ord(' '))
    return cleartexts

def is_space(lines: list[list[int]], current: list[int], i: int) -> bool:
    """
    Check if the current byte in the ciphertext represents an encrypted space character.
    
    Args:
        lines (list[list[int]]): The list of ciphertext byte arrays.
        current (list[int]): The current ciphertext byte array.
        i (int): The column index to check.
    
    Returns:
        bool: True if the byte is an encrypted space character, False otherwise.
    """
    for line in lines:
        result = line[i] ^ current[i]
        # Check if the result is a letter or both are spaces (result is 0)
        if not (chr(result).isalpha() or result != 0):
            return False
    return True

def dehex(hex_string: str) -> list[int]:
    """
    Converts a hexadecimal string to a list of byte values.
    
    Args:
        hex_string (str): The hexadecimal string to convert.
    
    Returns:
        list[int]: The list of byte values.
    """
    bytes_data = []
    for i in range(0, len(hex_string), 2):
        bytes_data.append(int(hex_string[i:i+2], 16))
    return bytes_data

def get_key_from_cipher_and_plaintext(cipher_hex: str, plaintext: str) -> str:
    """
    Derives the encryption key from a given ciphertext and the corresponding plaintext.
    
    Args:
        cipher_hex (str): The hexadecimal representation of the ciphertext.
        plaintext (str): The plaintext corresponding to the ciphertext.
    
    Returns:
        str: The derived key as a hexadecimal string.
    """
    cipher_bytes = dehex(cipher_hex)
    key = ""
    
    for i in range(len(plaintext)):
        key_byte = cipher_bytes[i] ^ ord(plaintext[i])
        key = key + f'{key_byte:02x}'
    
    return key

def get_message_from_cipher_and_key(cipher_hex: str, key_hex: str) -> str:
    """
    Decrypts a ciphertext using the provided key.
    
    Args:
        cipher_hex (str): The hexadecimal representation of the ciphertext.
        key_hex (str): The hexadecimal representation of the key.
    
    Returns:
        str: The decrypted message.
    """
    cipher_bytes = dehex(cipher_hex)
    key_bytes = dehex(key_hex)
    message = ""

    for i in range(len(cipher_bytes)):
        message_byte = chr(cipher_bytes[i] ^ key_bytes[i])
        message = message + message_byte
    return message

# Example usage
ciphertexts_hex = [
    "F9B4228898864FCB32D83F3DFD7589F109E33988FA8C7A9E9170FB923065F52DD648AA2B8359E1D122122738A8B9998BE278B2BD7CF3313C7609",
    "F5BF229F8F9B1C8832C0212DFD7F92EA18FF29C7E6C968848D6EFAC16074F129D640AB67CE59E3DC6109212AB4EB959FFD34F3B269EB292C7409",
    "FDAF668499C801C734813F3BF3718FF91AEA2C88FC862B999D6EE7C16369F83ADF57FF28CD18FCCC6F0D2B2BB5A295DEF436B0A164EF3C267014",
    "FDFB35858B8403882EC4392CE03289F50CF82588FC816ECB8B63F3843076F52CC059B035C718E0DB220D3B33B3A28692F478B2B07EF03D216B09",
    "E4BE239FCA9A0ADE29C43869FD74DBE31CE835DAE19D72CB9567FD897168FD2CDE5DFF35C65CFAD667136E29B2A7989BE339B1BA71F63C267A09",
    "F8BE279F848101CF60C9203EB26694B00EF929DCEDC9788E9B77EC843075FB39C759BE35C618E6C622016E31A2A8938DE239A1AA3DEC23267316",
    "E7BE2598988D4FC325D86F2CEA7193F117EC2588E19A2B859D67FA847426F230C10EAC3ECE55EAC170092D7FACAE8FDEF436B0A164EF3C267014",
    "E7BE259898811BD160C03B69E67A9EB01CF330CDE69A6ECB9764BE946367F636DF47AB3E835BE0C06E046E3BA6A69799F478A0B67EEA3A266B03"
]

ciphertexts = [dehex(hex_str) for hex_str in ciphertexts_hex]
cleartext = decypher(ciphertexts)
for line in cleartext:
    print("".join(line))

# Deriving key example
cipher_hex_example = "F9B4228898864FCB32D83F3DFD7589F109E33988FA8C7A9E9170FB923065F52DD648AA2B8359E1D122122738A8B9998BE278B2BD7CF3313C7609"
plaintext_example = "Modern cryptography requires careful and rigorous analysis"

key = get_key_from_cipher_and_plaintext(cipher_hex_example, plaintext_example)

# Decrypt messages using the derived key
for m in ciphertexts_hex:
    message = get_message_from_cipher_and_key(m, key)
    print(message)