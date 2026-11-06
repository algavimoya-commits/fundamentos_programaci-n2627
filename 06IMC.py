#Calculo de indice de masa coroporal

# Datos personales

peso = 88.9
altura = 1.84

# Calculo de IMC

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")