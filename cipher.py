class Cipher:

    def encrypt_caesar(self, string, shift): 
        if not isinstance(shift, int):
           raise TypeError("Invalid - must enter an integer for shift")

        encrypted = ''
        for char in string: 
            if char == ' ':
                encrypted = encrypted + char
            elif char.islower():
                encrypted = encrypted + chr((ord(char) + shift - 97) % 26 + 97)
            elif  char.isupper():
                encrypted = encrypted + chr((ord(char) + shift - 65) % 26 + 65)
            elif char.isdigit():
                encrypted = encrypted + char
            else:
                encrypted = encrypted + char
        return encrypted 

    def decrypt_caesar(self, string, shift): 
        translated = ''
        for char in string: 
            if char == ' ':
                translated = translated + char
            elif char.islower():
                translated = translated + chr((ord(char) - shift - 97) % 26 + 97)
            elif  char.isupper():
                translated = translated + chr((ord(char) - shift - 65) % 26 + 65)
            elif char.isdigit():
                translated = translated + char
            else:
                translated = translated + char
        return translated
