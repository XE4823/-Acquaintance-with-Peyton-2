n = int(input('Введите количество монет:'))
Gerb = 0
Reshka = 0
for i in range(n):
    i = int(input('Введите сторону монеты(1/0):'))
    if i == 1:
        Gerb += 1
    else:
        Reshka += 1
if Gerb < Reshka:
    print(Gerb)
else:
    print(Reshka)