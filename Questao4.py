def adicionarImposto(p, i):
  total = p + (p * i/100)
  print(f'R${total}')

c = int(input('Digite o preço do produto: '))
a = int(input('Digite a taxa: '))
adicionarImposto(c, a)
