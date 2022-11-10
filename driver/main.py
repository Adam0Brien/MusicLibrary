from models import Song, Playlist, MyMusicLibrary

allSongsList = []

library = MyMusicLibrary.MyMoviesLibrary("Adams Library", playlistList=[], allSongsList=allSongsList)


def validateInput(choice, min, max):
    if choice in range(min, max):
        return True
    else:
        return False


def mainMenu():
    print("Music Library")
    print("1) Add a Song")
    print("2) List all Songs")

    option = int(input("---->"))

    while not validateInput(option, 1, 10):
        option = int(input("---->"))
    if option == 1:
        addSong()
    if option == 2:
        listSongs()
    if option > 2:
        print("Please enter a valid option")
        mainMenu()


def addSong():
    name = input("Song name: ")
    group = input("Group/Artist Name: ")
    year = input("Year: ")
    genre = input("Genre: ")
    playlist = input("Playlist: ")
    newSong = Song.Song(name, group, year, genre, playlist)
    print(newSong.toString())
    allSongsList.append(newSong)

    mainMenu()


# TODO
def addPlaylist():
    playlistName = input("Playlist name: ")
    songsList = []

    newPlaylist = MyMusicLibrary.MyMoviesLibrary.addPlaylist(playlistName, songsList)

    mainMenu()


# TODO
def addSongToPlaylist():
    mainMenu()


def listSongs():
    for song in allSongsList:
        print(song.toString())


def startup():
    print(library.getUsername())  # Confirming the correct music library object is loaded


if __name__ == '__main__':
    startup()
    mainMenu()
