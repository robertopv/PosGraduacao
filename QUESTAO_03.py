# função para perguntar as dimensões do objeto
def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            volume = altura * largura * comprimento
            if volume < 1000:
                return 10
            elif volume < 10000:
                return 20
            elif volume < 30000:
                return 30
            elif volume < 100000:
                return 50
            else:
                print("Não é possível realizar o transporte de objetos com volume igual ou superior a 100.000 cm³.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")

# função para perguntar o peso do objeto
def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            if peso <= 0.1:
                return 1
            elif peso < 1:
                return 1.5
            elif peso < 10:
                return 2
            elif peso < 30:
                return 3
            else:
                print("Não é possível realizar o transporte de objetos com peso igual ou superior a 30 kg.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")

# função para perguntar a rota do objeto
def rotaObjeto():
    while True:
        rota = input("Digite a rota do objeto (RS, SR, BS, SB, BR, RB): ")
        if rota in ["RS", "SR", "BS", "SB", "BR", "RB"]:
            if rota in ["RS", "SR", "BS", "SB"]:
                return 1
            else:
                return 1.5
        else:
            print("Rota inválida. Por favor, digite uma rota válida.")


# Identificação
print("Bem vindo a companhia de logistica Roberto Pereira do Vale")
print("------------------------------------------- ")

# perguntar as dimensões do objeto
mult_dimensoes = dimensoesObjeto()

# perguntar o peso do objeto
mult_peso = pesoObjeto()

# perguntar a rota do objeto
mult_rota = rotaObjeto()

# calcular o valor do frete
valor_frete = 10 * mult_dimensoes * mult_peso * mult_rota

# exibir o valor do frete
print("O valor do frete é R$ %.2f." % valor_frete)
