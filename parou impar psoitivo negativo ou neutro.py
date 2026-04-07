n1n = int(input("digite o primeiro número aqui: "))
if ((n1n % 2 == 0) and (n1n > 0)):
    print("par positivo") 
elif ((n1n % 2 == 0) and (n1n < 0)):
    print("par negativo")
elif ((n1n %2!= 0) and (n1n>0)):
    print("ímpar positivo")
elif ((n1n%2!=0) and (n1n<0)):
    print("ímpar negativo")
elif(n1n == 0 ):
    print("neutro")