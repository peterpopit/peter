import random
print("загаданно случайное число от 0 до 100")
a = random.randint(0,100)
print("введите ваше число")
while True:
    b = int(input())
    if a == b:
        print("вы победили")
        
    else:
        print(" вы не угадали, попробуйте еще раз")

  
