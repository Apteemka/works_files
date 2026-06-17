with open("resources/secret.txt", 'r') as file:
    secret = file.read()
alphabet = ' abcdefghijklmnopqrstuvwxyz'
len_alp=len(alphabet)
subst = dict(zip(alphabet, alphabet[3:] + alphabet[:3]))
res = ''.join(map(subst.__getitem__, secret))
print('Result: ', '"',''.join(res),'"', sep = '')