def encode(key, message):
    zasifrovanytext = ""
    for char in message:
        if char.isalpha():
            text = char.isupper()
            char = char.upper()
            hodnota = ord(char) + key
            if hodnota > ord('Z'):
                hodnota -= 26
            char = chr(hodnota)
            if not text:
                char = char.lower()
        zasifrovanytext += char
    return zasifrovanytext

def decode(key, message):
    return encode(-key, message)

klic = 1
zprava = input("zadejte text pro šifrování: ")

šifrovaná_zpráva = encode(klic, zprava)
print(f"šifrovaná zpráva: {šifrovaná_zpráva}")

původní_zpráva = decode(klic, šifrovaná_zpráva)
print(f"původní zpráva: {původní_zpráva}")