n1k = int(input("Digite o primeiro número aqui: "))
n2k = int(input("Digite o segundo número aqui: "))
n3k = n1k + n2k

print("a soma entre eles é: ",n3k)
if (n1k == n2k):
    print("eles são iguais")
elif (n1k > n2k):
    print("o maior é: ",n1k)
else:
    print("o maior é: ",n2k)