def Desaider() -> bool: # bool - подкласс int
    playerChoise = input("Орёл или Решка?\n") # Ввод пользователя с клавиатуры
    return playerChoise == "орёл" # Результат сравнения с функцией
def IsWin(coin:str, playerChoise:bool):
    if coin == playerChoise: # Если значение выпавшей строны монеты совпадёт с игроком, то будет победа
        print("Победа")
    else:
        print("Поражение")
def Main():
    import random
    coin = random.randint(0,1) # Диапазон выбора для монет игрока 0 - Орёл, 1 - Решка
    playerChoise = Desaider() # выбор игрока
    IsWin(coin, playerChoise) 
Main()