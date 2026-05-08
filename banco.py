N = int(input("insira "))
saldo = int(input("saldo "))
menor_saldo = saldo

for count in range(int(N)):
    x = int(input())
    saldo = saldo + x
    if saldo < menor_saldo:
      menor_saldo = saldo
 
print(menor_saldo)
