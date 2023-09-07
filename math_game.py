attempts = 0
correct = 0
print('\033[1;34;48m === MATH GAME === \033[0m')
i = int(input('Name your multiples: '))
for num1 in range(10):
    attempts += 1
    print(attempts, 'x', i, '=')
    a = int(input(''))
    if a != attempts * i:
        print('Nope, the answer was', attempts * i)
    else:
        print('Great, well done!')
        correct += 1
print()
if correct == 10:
    print('\033[7;49;36m Strike! 10 out of 10 \033[0m')
elif correct >= 8:
    print('\033[7;49;32m You scored', correct, 'out of 10. So close! \033[0m')
elif correct > 4:
    print('\033[7;49;33m You scored', correct, 'out of 10! \033[0m')
else:
    print('\033[7;49;31m You scored', correct, 'out of 10! \033[0m')