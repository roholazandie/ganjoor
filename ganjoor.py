import sqlite3
from data_elements import Poem, Verse


class Ganjoor:

    def __init__(self):
        connection = sqlite3.connect("ganjoor.s3db")
        self.cursor = connection.cursor()

    def _convert_to_full_poem(self, verses):
        verses = [Verse(int(verse[0]), verse[1]) for verse in verses]
        poems = []
        poem_verses = []
        for verse in verses:
            if verse.number == 1:
                poem = Poem(title="", verses=poem_verses)
                poems.append(poem)
                poem_verses = []
                poem_verses.append(verse)
            else:
                poem_verses.append(verse)
        poems = poems[1:]
        return poems

    def get_poems(self, poet_name):
        sql = f"""select vorder, text
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
                                        where name = {poet_name}
                                    )
                          )


                        )"""
        result = self.cursor.execute(sql)
        verses = result.fetchall()
        poems = self._convert_to_full_poem(verses)
        return poems


if __name__ == "__main__":
    ganjoor = Ganjoor()
    poems = ganjoor.get_poems('\'حافظ\'')
    print([verse.text for verse in poems[0].verses])
