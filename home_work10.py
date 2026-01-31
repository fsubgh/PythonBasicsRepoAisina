import sqlite3

connection = sqlite3.connect('electronics_store.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')

items = [
    ('Laptop', 1200.50, 5),
    ('Phone', 800.00, 10),
    ('Tablet', 300.00, 0)
]
cursor.executemany('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', items)
connection.commit()
print("Записи добавлены.")


cursor.execute('UPDATE products SET quantity = ? WHERE name = ?', (10, 'Laptop'))
connection.commit()
print("Количество Laptop обновлено.")


cursor.execute('DELETE FROM products WHERE quantity = 0')
connection.commit()
print("Товары с нулевым остатком удалены.")


print("\nИтоговый список товаров в базе:")
cursor.execute('SELECT name, price, quantity FROM products')
for row in cursor.fetchall():
    print(f"Товар: {row[0]}, Цена: {row[1]}, Кол-во: {row[2]}")

connection.close()

