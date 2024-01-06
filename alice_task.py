import simplecrypt


with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    for password in open("passwords.txt"):
        try:
            decrypted = simplecrypt.decrypt(password.strip(), encrypted).decode("utf8")
        except simplecrypt.DecryptionException:
            continue
        print(decrypted)
