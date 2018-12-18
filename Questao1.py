def imprimirEscada(n):
  i = 0
  while i <= n:
    print(f' {i} ' * i)
    i += 1

n = int(input('Digite um valor: '))
imprimirEscada(n)
