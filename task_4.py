with open("resources/secret.txt", 'r') as file:
    secret = file.read()
secret.lower()
alphabet = ' abcdefghijklmnopqrstuvwxyz'
len_alp = len(alphabet)
subst = dict(zip(alphabet, alphabet[3:] + alphabet[:3]))
enc = ''.join(map(subst.__getitem__, secret))
with open("resources/encrypted.txt", 'w+') as file:
    file.write(enc)
    subst = dict(zip(alphabet, alphabet[-3:] + alphabet[:-3]))
    dec = ''.join(map(subst.__getitem__, enc))
with open("resources/decrypted.txt", 'w') as file:
    file.write(dec)
print('Result: ', '"',''.join(enc),'"', sep = '')