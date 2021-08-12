from db import connection


def create(title, content, author, date):
    # открываем соединение с бд, чтобы записывать изменения
    db = connection.make()
    try:
        # Объект взаимодействия с бд
        cursor = db.cursor()
        # сам запрос
        sql = "INSERT INTO articles (title, content, author, date) values (%s, %s, %s, %s)"
        # Выполняем запрос
        cursor.execute(sql, (title, content, author, date))
        # сохраняем изменения в бд
        db.commit()
        # возвращаем результат успешного выполнения
        return True
    except Exception as error:
        # возвращаем содержание ошибки
        return error
    finally:
        # закрытие соединения с бд
        db.close()


'''
%s в запросе нужен для того, чтобы обезопасить запрос и не напрямую подставлять
данные из переменных в строку, а пропустить их через специальный механизм, который заменит эти символы на
данные, и очистит эти данные от возможных опасных символов.
'''


def read_one(article_id):
    # открываем соединение с бд, чтобы записывать изменения
    db = connection.make()
    try:
        # Объект взаимодействия с бд
        cursor = db.cursor()
        # запрос
        sql = "SELECT * FROM articles where id=%s"
        # выполняем запрос
        cursor.execute(sql, (article_id))
        # Возвращаем словарь с заданной записью
        return cursor.fetchone()

    except Exception as error:
        # возвращаем содержание ошибки
        return error
    finally:
        # закрытие соединения с бд
        db.close()


def read_many(how_many):
    # открываем соединение с бд, чтобы записывать изменения
    db = connection.make()
    try:
        # Объект взаимодействия с бд
        cursor = db.cursor()
        # запрос
        sql = "SELECT * FROM articles"
        # выполняем запрос
        cursor.execute(sql)
        # Возвращаем словарь с заданным количеством записей
        return cursor.fetchmany(how_many)

    except Exception as error:
        # возвращаем содержание ошибки
        return error
    finally:
        # закрытие соединения с бд
        db.close()


def read_all():
    # открываем соединение с бд, чтобы записывать изменения
    db = connection.make()
    try:
        # Объект взаимодействия с бд
        cursor = db.cursor()
        # запрос
        sql = "SELECT * FROM articles"
        # выполняем запрос
        cursor.execute(sql)
        # Возвращаем словарь сo всеми записями
        return cursor.fetchall()

    except Exception as error:
        # возвращаем содержание ошибки
        return error
    finally:
        # закрытие соединения с бд
        db.close()


def update(article_id, title, content, author, date):
    # открываем соединение с бд, чтобы записывать изменения
    db = connection.make()
    try:
        # Объект взаимодействия с бд
        cursor = db.cursor()
        # запрос
        sql = "UPDATE articles SET title=%s, content=%s, author=%s, date=%s WHERE id=%s"
        # выполняем запрос
        cursor.execute(sql, (title, content, author, date, article_id))
        # Сохраняем изменения
        db.commit()
        # возвращаем результат
        return True

    except Exception as error:
        # возвращаем содержание ошибки
        return error
    finally:
        # закрытие соединения с бд
        db.close()


def delete(article_id):
    # открываем соединение с бд, чтобы записывать изменения
    db = connection.make()
    try:
        # Объект взаимодействия с бд
        cursor = db.cursor()
        # запрос
        sql = "DELETE FROM articles WHERE id=%s"
        # выполняем запрос
        cursor.execute(sql, (article_id))
        # Сохраняем изменения
        db.commit()
        # возвращаем результат
        return True

    except Exception as error:
        # возвращаем содержание ошибки
        return error
    finally:
        # закрытие соединения с бд
        db.close()


def delete_all():
    # открываем соединение с бд, чтобы записывать изменения
    db = connection.make()
    try:
        # Объект взаимодействия с бд
        cursor = db.cursor()
        # запрос
        sql = "DELETE FROM articles"
        # выполняем запрос
        cursor.execute(sql)
        # Сохраняем изменения
        db.commit()
        # возвращаем результат
        return True

    except Exception as error:
        # возвращаем содержание ошибки
        return error
    finally:
        # закрытие соединения с бд
        db.close()
