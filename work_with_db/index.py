import psycopg2

conn = psycopg2.connect(dbname="test", user="postgres", password="231284")

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS superheroes")
cur.execute("DROP TABLE IF EXISTS traffic_light")

conn.commit()

cur.execute("CREATE TABLE superheroes (hero_id serial PRIMARY KEY, hero_name varchar, strength int")
cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)", ("Superman", 100))

# BIG NO
# cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)" % ("Superman", 100))

# Второй вариант добавления данных в БД:

cur.execute("""
            INSERT INTO superheroes (hero_name, strength)
            VALUES (%(name)s, %(strength)s);
            """, {'name': 'Green Arrow', 'strength': 80})

conn.commit()


