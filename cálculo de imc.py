# e) cálculo de imc
altura = float(input("Digite aqui a sua altura, em metro: "))
peso = float(input("Digite aqui o seu peso, em kg: "))
imc = peso / (pow(altura,2))

print("O seu IMC é: ", imc)