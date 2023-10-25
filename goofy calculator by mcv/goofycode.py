import os
print("--- GOOFY CALCULATOR ---")
def goofy():
    while True:
        while True:
            first=input("Input first number: ")
            if first.isdigit(): break
            else: pass
        while True:
            second=input("Input second number: ")
            if second.isdigit(): break
            else: pass
        while True:    
            i=input("Choose the operation: +,-,*,/: ")
            if i=='/':
                print(f'{first} {i} {second} = {(int(second)+int(first))/2}')
                break
            elif i=='*':
                print(f'{first} {i} {second} = {int(first)**int(second)}')
                break
            elif i=='+':
                print(f'{first} {i} {second} = {str(first)+str(second)}')
                break
            elif i=='-':
                print(f'{first} {i} {second} = {str(second)+str(first)}')
                break
            else: pass
        while True:
            yn=input("Type a for again, e for exit: ")
            if yn=='a':
                os.system('cls')
                print("--- GOOFY CALCULATOR ---")
                break
            elif yn=='e':
                exit()
            else: pass

goofy()