choises = ["Камень", "Ножницы","Бумага"]
user_choises: int = input("Выбери: камень, ножницы или бумага")
computer_choises: int = input("камень")
if user_choises == computer_choises:
    print("Ничья!")
elif (user_choises == "камень" and computer_choises == "ножницы") or (user_choises == "ножницы" and computer_choises == "бумага") or (user_choises == "бумага" and computer_choses == "камень"):
    print("Ты выиграл!")
else:
    print("Ты проиграл(")
computer_choises: int = input("ножницы")
if user_choises == computer_choises:
    print("Ничья!")
elif (user_choises == "камень" and computer_choises == "ножницы") or (user_choises == "ножницы" and computer_choises == "бумага") or (user_choises == "бумага" and computer_choses == "камень"):
    print("Ты выиграл!")
else:
    print("Ты проиграл(")
computer_choises: int = input("бумага")
if user_choises == computer_choises:
    print("Ничья!")
elif (user_choises == "камень" and computer_choises == "ножницы") or (user_choises == "ножницы" and computer_choises == "бумага") or (user_choises == "бумага" and computer_choses == "камень"):
    print("Ты выиграл!")
else:
    print("Ты проиграл(")