alphabet = " abcdefghijklmnopqrstuvwxyz"
key = 3
s = "i am caesar"
subst = dict(zip(alphabet, alphabet[key:]+alphabet[:key]))
res = ''.join(map(subst.__getitem__, s))
print('Result: "' + res + '"') # Result: "lcdpcfdhvdu"