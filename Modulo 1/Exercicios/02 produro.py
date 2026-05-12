nome_do_produto = input("Digite o nome do produto: ") 
preço = float (input ("digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto"))
valor_desconto = preço * desconto /100 
preço_final = preço - valor_desconto
print (f"produto: {nome_do_produto} - Preço final: R$ {preço_final}") 