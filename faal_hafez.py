import sqlite3
import random
from utils import convert_to_full_poem

connection = sqlite3.connect("ganjoor.s3db")
cursor = connection.cursor()

sql = """select vorder, text
            from verse
            where poem_id IN (
                select id
                from poem
                where cat_id IN
                  (
                      select id
                      from cat
                      where poet_id IN
                            (
                                select id
                                from poet
                                where name = 'حافظ'
                            )
                  )
            
            
                )"""


result = cursor.execute(sql)
verses = result.fetchall()
poems = convert_to_full_poem(verses)
faal_id = random.randint(0, len(poems))
faal = poems[faal_id]
for verse in faal:
    print(verse)