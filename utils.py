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