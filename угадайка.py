import random

colors = ['красный', 'синий', 'зеленый', 'желтый', 'розовый']

def generate_colors(colors):
    return [random.choice(colors) for _ in range(4)]

def validate_user_input(user_colors,colors):
    if len(user_colors)!=4:
        print("Вы ввели неправильное количество цветов! Нужно ввести ровно 4")
        return False
    
    for color in user_colors:
        if color not in colors:
            print(f"{color} - неверный цвет. Допустимые цвета: {', '.join(colors)}")
            return False
    
    return True

def compare_codes(generate_colors,user_guess):
    correct_position = sum(1 for i in range(4) if generate_colors[i] == user_guess[i])
    correct_color = sum(min(generate_colors.count(color),user_guess.count(color)) for color in set(user_guess))

    incorrect_position = correct_color - correct_position
    
    return correct_position, incorrect_position

def play_game():
    comp = generate_colors(colors)
    
    attempts = 0
    
    while True:
         user_guess = input("\nВведите вашу комбинацию из 4-х цветов через пробел: ").split()
         if not validate_user_input(user_guess, colors):
             continue
         attempts += 1 
         
         correct_position, incorrect_position = compare_codes(comp, user_guess)
         
         if correct_position == 4:
             break
         
         print(f"Правильные цвета в правильной позиции: {correct_position}")
         print(f"Правильные цвета в неправильной позиции: {incorrect_position}")
         
    print(f"\nПоздравляем! Вы справились за {attempts} попыток!")
    
if __name__ == "__main__":
    print("Добро пожаловать в Mastermind! Угадайте комбинацию из 4-х цветов:")
    print(f"Доступные цвета: {', '.join(colors)}")
    play_game()