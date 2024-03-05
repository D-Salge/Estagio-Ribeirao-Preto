def inverte_string(s):
    s_invertida = ''
    for caracter in s:
        s_invertida = caracter + s_invertida
    return s_invertida

s = input("Digite uma string: ")
print("String invertida:", inverte_string(s))
