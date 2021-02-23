from cipher import Cipher

cipher = Cipher()

code = cipher.encrypt_caesar("abcABC123xyzXYZ", 2)
code1 = cipher.encrypt_caesar("Hello how are you today??£$%^", 5)
print(code1)
print()
print("Encrypting:")
print(f"abcABC123xyzXYZ -> {code}")
#Expect: cdeCDE123zabZAB

plain = cipher.decrypt_caesar("cdeCDE123zabZAB", 2)

print()
print("Decrypting:")
print(f"cdeCDE123zabZAB -> {plain}")
# Expect: abcABC123xyzXYZ

print()

code = cipher.encrypt_caesar("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", -3)

print()
print("Encrypting:")
print(f"THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG -> {code}")
# Expect: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

plain = cipher.decrypt_caesar("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD", -3)
plain2 = cipher.decrypt_caesar("Mjqqt mtb fwj dtz ytifd??£$%^", 5)
print(plain2)

print()
print("Decrypting:")
print(f"QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD -> {plain}")
# Expect: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG