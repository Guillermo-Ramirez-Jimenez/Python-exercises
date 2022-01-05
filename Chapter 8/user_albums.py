def make_album(artist, album, songs_count=None):
	album_dict={}
	album_dict['artist']=artist.title()
	album_dict['album']=album.title()
	if songs_count:
		album_dict['songs_count']=songs_count
	return album_dict

while True:
	print("\nEnter album info:\nEnter 'q' to quit:")
	artist=input("Enter artist: ")
	if artist=='q':
		break
	album=input("Enter album: ")
	if album=='q':
		break
	print(make_album(artist, album))