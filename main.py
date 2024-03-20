from victory import better_victory
from bank_account import personal_account
from file_manager import filemanagerfunc
import os


def main_func():
    while True:
        user_input = int(input('1. Создать папку \n2. Удалить файл/папку \n3. Копировать файл/папку'
          '\n4. Просмотреть содержимое рабочей директории \n5. Просмотреть папки \n6. Просмотреть файлы'
          '\n7. Информация об ОС \n8. Создатель программы \n9. Игра викторина \n10. Банквоский счет'
          '\n11. Смена директории \n12. Выход \nВведите пункт меню (цифру): '))
        if user_input in range(1, 8):
            filemanagerfunc(user_input)
        elif user_input == 8:
            print('Создатель программы: Окуньков Дмитрий')
        elif user_input == 9:
            better_victory()
        elif user_input == 10:
            personal_account()
        elif user_input == 11:
            dir_input = str(input('Введите название дирекотрии: '))
            os.chdir(dir_input)
        else:
            break


main_func()
