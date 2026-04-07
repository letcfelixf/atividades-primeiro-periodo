n1j = int(input("digite o primeiro número aqui: "))
if ((n1j % 2 == 0) and (n1j > 0)):
    print("par positivo") 
elif ((n1j % 2 == 0) and (n1j < 0)):
    print("par negativo")
else: 
    print("ímpar")