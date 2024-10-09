#Kaja Matuszewska 345951
#Lista 1 Zadanie 2

def is_palindrom(text):
    text = ''.join(c.lower() for c in text if c.isalnum())
    
    for i in range(len(text) // 2):
        if text[i] != text [-(i + 1)]:
            return False
        
    return True

print(is_palindrom("palindrom"))
print(is_palindrom("kajak"))
print(is_palindrom("Kobyła ma mały bok."))
print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))
print(is_palindrom("Míč omočím."))