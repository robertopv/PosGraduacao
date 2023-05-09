cardapio = {
    100: {"descricao": "Cachorro-Quente........", "valor": 09.00},
    101: {"descricao": "Cachorro-Quente Duplo..", "valor": 11.00},
    102: {"descricao": "X-Egg..................", "valor": 12.00},
    103: {"descricao": "X-Salada...............", "valor": 13.00},
    104: {"descricao": "X-Bacon................", "valor": 14.00},
    105: {"descricao": "X-Tudo.................", "valor": 17.00},
    200: {"descricao": "Refrigerante Lata......", "valor": 05.00},
    201: {"descricao": "Chá Gelado.............", "valor": 04.00}
}
print("Bem vindo a Lanchonete do Roberto Pereira do Vale")
print("------------------------------------------- ")
print("----------------Cardápio----------------")
for codigo, produto in cardapio.items():
    print(f"Código: {codigo} - {produto['descricao']}  : R${produto['valor']:.2f}")
print("-----------------------------------------")
valor_total = 0.0
while True:
    try:
        codigo = int(input("Digite o código do produto desejado: "))

        if codigo not in cardapio:
            print("Opção inválida! Por favor, escolha um código válido.")
            continue
        valor_total += cardapio[codigo]["valor"]

        print(f"Item adicionado ao pedido: {cardapio[codigo]['descricao']} (R$ {cardapio[codigo]['valor']:.2f})")
        opcao = input("Deseja pedir mais alguma coisa? (S/N) ").upper()
        if opcao == "N":
            break
    except ValueError:
        print("Opção inválida! Por favor, escolha um código válido.")
        continue

print(f"\nTotal a pagar: R$ {valor_total:.2f}")
