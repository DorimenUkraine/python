import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname='test', user='postgres',
                        password='231284', host='localhost')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS superheroes")
cur.execute("DROP TABLE IF EXISTS traffic_light")

conn.commit()

cur.execute("CREATE TABLE superheroes (hero_id serial PRIMARY KEY, hero_name varchar, strength int)")
cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)", ("Superman", 100))
cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)", ("Flash", 999))

# BIG NO
# cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)" % ("Superman", 100))

# Второй вариант добавления данных в БД:

cur.execute("""
            INSERT INTO superheroes (hero_name, strength)
            VALUES (%(name)s, %(strength)s);
            """, {'name': 'Green Arrow', 'strength': 80})

conn.commit()

cur.execute("CREATE TABLE traffic_light (light_id serial PRIMARY KEY, light text);")

# WRONG USAGE

# cur.execute("INSERT INTO traffic_light (light) VALUES ('%s')", (10,)) - нельзя кавычки '%s'
# cur.execute("INSERT INTO traffic_light (light) VALUES ('%d')", (10,)) - нельзя d '%d'
# cur.execute("INSERT INTO traffic_light (light) VALUES ('%s')", (10)) - в передаваемых данных, даже если одно, кавычки 10,

cur.execute("INSERT INTO traffic_light(light) VALUES (%s)", ("red",))

cur.execute("SELECT * FROM superheroes")

one_line = cur.fetchone()
print(one_line)

full_fetch = cur.fetchall()

for record in full_fetch:
    print(record)

# full_fetch[0][0]

conn.commit()

cur.close()
conn.close()

with psycopg2.connect(dbname='test', user='postgres', password='231284', host='localhost') as conn:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as curs:

        curs.execute.values(curs, "INSERT INTO traffic_light(light) VALUES %s", [("green",), ("yellow",)])

        curs.execute("SELECT * FROM traffic_light")
        records = curs.fetchall()
        print(records)
        print(records[0]["light"])

