#利用filter函数过滤分数大于96的值

pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]
print(pp)

def a(i):
    if i[1] >= 96:
        return True
    else:
        return False

print(list(filter(a,pp)))
