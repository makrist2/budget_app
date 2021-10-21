import sqlite3


CREATE_FOOD = "CREATE TABLE IF NOT EXISTS food (id INTEGER PRIMARY KEY,item TEXT, price INTEGER, date DATE);"
CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other (id INTEGER PRIMARY KEY,item TEXT, price INTEGER, date DATE);"

INSERT_FOOD = "INSERT INTO food (item, price, date) VALUES(?,?,?);"
INSERT_OTHER = "INSERT INTO other (item, price, date) VALUES(?,?,?);"

SELECT_ALL_FOOD = "SELECT * FROM food;"
SELECT_ALL_OTHER = "SELECT * FROM other;"

DELETE_ALL_FOOD = "DELETE FROM food"
DELETE_ALL_OTHER = "DELETE FROM other"


def create_tables():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_OTHER), conn.execute(CREATE_FOOD)


def insert_food(item, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_FOOD, (item, price, date))
        conn.commit()


def insert_other(item, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_OTHER, (item, price, date))
        conn.commit()
        c.close()


def select_all_food():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_FOOD)
        lst = c.fetchall()
        c.close()
        output = ''
        for x in lst:
            output = output + f'Food name: {str(x[1])}, Food price: {str(x[2])}, Purchase date: {str(x[3])}\n'
        return output


def select_all_other():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_OTHER)
        lst = c.fetchall()
        c.close()
        output = ''
        for x in lst:
            output = output + f'Item name: {str(x[1])}, Item price: {str(x[2])}, Purchase date: {str(x[3])}\n'
        return output


def select_food_price_sum():
    conn = sqlite3.connect('data.db')
    sum = 0
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_FOOD)
        lst = c.fetchall()
        for x in lst:
            sum += x[2]
        return sum


def select_other_price_sum():
    conn = sqlite3.connect('data.db')
    sum = 0
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL_OTHER)
        lst = c.fetchall()
        for x in lst:
            sum += x[2]
        return sum


def delete_food():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_ALL_FOOD)
        conn.commit()
        c.close()


def delete_everything():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_ALL_FOOD)
        c.execute(DELETE_ALL_OTHER)
        conn.commit()
        c.close()


def delete_other():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_ALL_OTHER)
        conn.commit()
        c.close()


create_tables()
