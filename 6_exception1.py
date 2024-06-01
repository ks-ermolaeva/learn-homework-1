"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

  Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            user_say = input('Как дела? ')
        except KeyboardInterrupt:
            print('Пока!')
            break
        if user_say.lower() == 'хорошо':
            break

if __name__ == "__main__":
    hello_user()
