tabuada=int(input("Digite um numero para exibir a tabuada: "))
print("Tabuada do numero: ", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))
