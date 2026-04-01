# atividades de operadores lógicos
resposta1 = input("Você quer ver os resultados? ")

if resposta1 == "sim":
#a)
   print((2 > 3) and (5 != 0))
 #false - certo
#b)
   print((4 < 10) and (3 == 3))
 #true - certo
#c)
   print((7 >= 7) or (2 > 5))
 #true - certo
#d)
   print(not (3 < 1) and (6 == 6))
 #true - certo
#e)
   print((8 != 8) or (10 > 2))
 #true - certo
#f) 
   print(not (5 > 3 and 2 < 1))
 #true - certo
#g)
   print((9 > 5) and not (4 == 4))
 #false - certo
#h) 
   print((6 < 2) or (3 != 3) or (1 == 1))
 #true - certo
#i) 
   print(not (2 > 1) or (5 >= 5 and 3 < 4))
 #true - certo
#j)
   print((10 != 10) and (not (2 < 3) or (8 > 1)))
 #false - certo
#k)
   print((10 > 5) and ("a" == "a"))
 #true - certo
#l) 
   print(("python" != "Python") or (3 * 2 == 6))
 #true - certo
#m)
   print((4 + 1 == 6) or ("chat" == "chat"))
 #true - certo
 
else:
   print("então acabou!")