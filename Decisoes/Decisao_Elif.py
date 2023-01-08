nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()
if idade>=65:
    print("O paciente " +nome +" POSSUÍ atendimento prioritário")
elif doenca_infectocontagiosa=="SIM":
    print("O paciente: "+ nome +" Deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente: "+ nome +" O paciente não possuí atendimento prioritário e pode aguardar na sala de espera comum!")
print("Fim!")