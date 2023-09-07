print('\033[1;34;48m === INTEREST CALCULATOR === \033[0m')
sum = 0
period = 0
percentage = 0
total_interest = 0
sum = float(input('Introduce loan sum: '))
period = int(input('Introduce period (In years): '))
percentage = float(input('Introduce annualy interest (in %): ')) / 100
for num in range(period):
    interest = sum * percentage

    total_interest += interest

    sum = sum + (sum * percentage)
    print('Year', num + 1, ':', round(sum, 2))
print()
print('\033[1;33;48m You paid', round(total_interest, 2),
      'in interest \033[0m')
