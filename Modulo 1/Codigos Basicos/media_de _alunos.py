nome = input ("Digite o nome do aluno:")
nota1 = float(input ("Digite a primeira nota:" ))
nota2 = float(input ("Digite a segunda nota:" ))
nota3 = float(input ("Digite a terceira nota:" ))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print(f"o aluno {nome} esta aprovado")
elif media >=4: 
  print(f"O aluno {nome} esta de recuperação ")
elif media <=3:
   print(f"o aluno {nome} esta reprovado")
