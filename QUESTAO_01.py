print("Bem vindo a loja do Roberto Pereira do Vale")
print("------------------------------------------- ")
try:
    valor_unitario = float(input("Digite o valor unitário do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
except ValueError:
    print("Erro: valor digitado inválido.")
else:
    valor_total_sem_desconto = valor_unitario * quantidade
    if quantidade < 10:
        valor_total_com_desconto = valor_total_sem_desconto
        percentual_desconto = "0%"
    elif quantidade < 100:
        valor_total_com_desconto = valor_total_sem_desconto * 0.95
        percentual_desconto = "5%"
    elif quantidade < 1000:
        valor_total_com_desconto = valor_total_sem_desconto * 0.9
        percentual_desconto = "10%"
    else:
        valor_total_com_desconto = valor_total_sem_desconto * 0.85
        percentual_desconto = "15%"


    print(f"Valor total sem desconto: R${valor_total_sem_desconto:.2f}")
    print(f"Valor total com desconto ({percentual_desconto} de desconto): R${valor_total_com_desconto:.2f}")
