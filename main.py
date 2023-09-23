import psycopg2

from api import  RequestsManager


connection = psycopg2.connect(
    database="json_19:30",
    user="postgres",
    password="123456",
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("""
DROP TABLE IF EXISTS categories;
CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    category_name VARCHAR(50)

);
""")

connection.commit()
# connection.close()

requests_manager = RequestsManager()
categories = requests_manager.get('/products/categories/')
for category in categories:
    cursor.execute("INSERT INTO categories(category_name) VALUES (%s)", (category,))
    connection.commit()






