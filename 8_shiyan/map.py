

pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]


def a(i):
    return i[0].lower()
L = list(map(a, pp))


print(L)
