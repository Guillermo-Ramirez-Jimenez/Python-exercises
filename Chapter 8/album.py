def make_album(artist, album, songs_count=None):
	album_dict={}
	album_dict['artist']=artist.title()
	album_dict['album']=album.title()
	if songs_count:
		album_dict['songs_count']=songs_count
	return album_dict

a=make_album("jean michel jarre", "equinoxe")
b=make_album("daft punk", "random access memories", 13)

print(a)
print(b)