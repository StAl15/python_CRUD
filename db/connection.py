import pymysql.cursors
from pymysql.cursors import DictCursor


# создадим функцию make, которая будет создавать соединение
# с БД и возвращать модуль, при помощи которого можно управлять нашей БД

def make(host="127.0.0.1", user="root", password="1EI2ALexM6%U",
         db="test_db", charset="utf8", cursorclass=DictCursor):
    connection = pymysql.connect(user=user, password=password, host=host, charset=charset,
                                 cursorclass=cursorclass, db=db)
    return connection


'''
Что тут происходит? В данную функцию передаются данные, необходимые для подключения к БД. Для подключения к
БД необходимы следующие аргументы:
- host (адрес) БД, по умолчанию это 127.0.0.1
- user (логин пользователь) БД, по умолчанию это root
- password (пароль пользователя) БД, его вы создавали сами, во время установки сервера MySQL
- db (имя БД), база данных с некоторым именем
- charset (кодировка данных) БД, по умолчанию ставьте utf-8, самая достойная кодировка
- cursorclass, определяет форму в которой данные будут возвращаться из БД. По умолчанию – список. Но я
импортировал DictCursor и передал его в качестве аргумента по умолчанию.
'''
