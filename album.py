def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs is not None:
        album["songs"] = songs
    return album

album1 = make_album("Pink Floyd", "The Dark Side of the Moon")
album2 = make_album("The Beatles", "Abbey Road")
album3 = make_album("Nirvana", "Nevermind", 12)

print(album1)
print(album2)
print(album3)

