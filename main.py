import sqlite3
import random

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

def convert_to_full_poem(verses):
    poems = []
    poem = []
    for verse in verses:
        if verse[0]==1:
            poems.append(poem)
            poem = []
            poem.append(verse[1])
        else:
            poem.append(verse[1])
    poems.remove([])
    return poems

result = cursor.execute(sql)
verses = result.fetchall()
poems = convert_to_full_poem(verses)
faal_id = random.randint(1, len(poems))
faal = poems[faal_id]
for verse in faal:
    print(verse)