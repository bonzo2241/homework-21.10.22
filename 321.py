a=int(input("Введите число"))
b=int(input("В двоичную или восьмеричную?(введите цифру)"))
c=''
if b == 2 or b == 8:
    while a>0:
        c= str(a % b) + c
        a //= b
    print(c)
else:
    print("Попробуйте ещё раз")
