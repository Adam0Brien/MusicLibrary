from models import Song, Playlist, MyMusicLibrary
import sys
import re
import urllib.request
import webbrowser

allSongsList = []
songsList = []

library = MyMusicLibrary.MyMusicLibrary("Adams Library", playlistList=[], allSongsList=allSongsList)
playlist1 = Playlist.Playlist("Adams Playlist", songsList)


def validateInput(choice, min, max):
    if choice in range(min, max):
        return True
    else:
        return False


def mainMenu():
    print("Music Library")
    print("1) Song Menu")
    print("2) Playlist Menu")
    print("3) Read in data from txt file")
    print("10) Exit")

    option = int(input("---->"))

    while not validateInput(option, 1, 10):
        option = int(input("---->"))
    if option == 1:
        songMenu()
    if option == 2:
        playlistMenu()
    if option == 3:
        readFromFile()
    if option == 10:
        exit()
    if option > 10:
        print("Please enter a valid option")
        mainMenu()



def songMenu():
    print("Songs Menu")
    print("1) Add a Song")
    print("2) List all Songs")
    print("3) Search song by name")
    print("4) List all songs of a certain genre")
    print("5) Search for song on Youtube")
    print("6) Remove a Song")
    print("10) Exit")

    option = int(input("---->"))

    while not validateInput(option, 1, 10):
        option = int(input("---->"))
    if option == 1:
        addSong()
    if option == 2:
        listSongs()
    if option == 3:
        searchSongs()
    if option == 4:
        genre = input("What Genre? ---->")
        displayGenre(genre)
    if option == 5:
        searchYoutube()
    if option == 6:
        deleteSongFromPlaylist()
    if option == 10:
        exit()
    if option > 10:
        print("Please enter a valid option")
        mainMenu()


def playlistMenu():
    print("Playlist Menu")
    print("1) Add a Playlist")
    print("2) List all Playlists")
    print("3) Add a song to a Playlist")
    print("4) List all songs in playlist")
    print("5) Remove a Playlist")

    option = int(input("---->"))

    while not validateInput(option, 1, 10):
        option = int(input("---->"))
    if option == 1:
        addPlaylistToLibrary()
    if option == 2:
        listPlaylists()
    if option == 3:
        addSongToPlaylist()
    if option == 4:
        listSongsInPlaylist()
    if option == 5:
        removeAPlaylist()
    if option > 10:
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

    try:
        f = open("songs.txt", "a")  # a mode will append to existing file contents
        f.write(newSong.txtString())
    except:
        print("Error: writing to the file")
    finally:
        f.close()  # close the file
    mainMenu()


# TODO
def addPlaylistToLibrary():
    playlistName = input("Playlist name: ")
    newSongsList = []
    newPlaylist = Playlist.Playlist(playlistName, newSongsList)

    # newPlaylist = MyMusicLibrary.MyMusicLibrary.addPlaylist(playlist1)
    library.addPlaylist(newPlaylist)

    listPlaylists()
    mainMenu()

def removeAPlaylist():
    for i, playlist in enumerate(library.getPlaylistList()):
        print(f"{i}: {playlist.getPlaylistName()}")

    selection = int(input("Enter the playlist you want to remove: "))
    library.removePlaylist(selection)



def addSongToPlaylist():
    for i, playlist in enumerate(library.getPlaylistList()):
        print(f"{i}: {playlist.getPlaylistName()}")

    for i,song in enumerate(allSongsList):
        print(f"{i}: {song.getTuneName()}")
    songIndex = int(input("Enter Which song to add: "))

    playlist.addSong(allSongsList[songIndex])



    mainMenu()


def listSongs():
    for song in allSongsList:
        print(song.toString())


def listPlaylists():
    for playlist in library.getPlaylistList():
        print(playlist.getPlaylistName())

def listSongsInPlaylist():
    for i, playlist in enumerate(library.getPlaylistList()):
        print(f"{i}: {playlist.getPlaylistName()}")

    # Get the user's selection
    selection = input("Enter the number of the list you want view: ")

    print_songs(library.getPlaylistByIndex(selection))

def print_songs(playlist):
    # Print the name of the playlist
    print(f"Playlist: {playlist.getPlaylistName()}")
    # Iterate over the songs in the playlist
    for i, song in enumerate(playlist.getSongsList()):
        # Print the title and artist of the song
        print(f"{i+1}. {song.getTuneName()} - {song.getTuneGroup()}")


def searchSongs():
    fname = "songs.txt"
    songName = input("What song are you looking for? --->")
    try:
        with open(fname, 'r') as myFile:
            found = 0
            index = 0
            for line in myFile:  # loop through file line by line
                index += 1

                if songName in line:
                    found = 1
                    break

            if found == 0:
                print('Song Name ', songName, ' not found in file')
            else:
                print('Song Name ', songName, ' found in file in line ', index)

            myFile.close()
    except:
        print("Error")


def displayGenre(genre):
    filtered_songs = [song.getTuneName() for song in allSongsList if song.getTuneGenre() == genre]

    for song in filtered_songs:
        print(song)

#TODO
def deleteSongFromPlaylist():
    for i, playlist in enumerate(library.getPlaylistList()):

        listSongsInPlaylist()
        selection = int(input("Enter the song you want to remove: ")) - 1

        library.removeSongFromPlaylist(playlist,selection)

    mainMenu()


def readFromFile():
    fname = input("Enter the name of the file you wish to open for reading: ")

    try:
        with open(fname, 'r') as myFile:
            for line in myFile:
                sName, sGroup, sYear, sGenre, sPlaylist = line.split(',')

                newSong = Song.Song(sName, sGroup, sYear, sGenre, sPlaylist)
                #print(newSong.toString())
                allSongsList.append(newSong)

    except:
        print("Error: reading from the file")
    finally:
        myFile.close()  # close the file

    mainMenu()


def searchYoutube():
    # https://codefather.tech/blog/youtube-search-python/
    fname = "songs.txt"
    songName = input("What song are you looking for? --->").casefold()
    try:
        with open(fname, 'r') as myFile:
            found = 0
            index = 0
            for line in myFile:  # loop through file line by line
                index += 1

                if songName in line.casefold():  # casefold ignores case sensitivity
                    found = 1
                    break

            if found == 0:
                print("")
                print('Song Name ', songName, ' not found in file, You cant search if you haven\'t added the song')
                print("")
                mainMenu()
            else:
                html = urllib.request.urlopen(
                    "https://www.youtube.com/results?search_query=" + songName.replace(" ", ""))
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                videoURL = "https://www.youtube.com/watch?v=" + video_ids[0]

                webbrowser.open_new_tab(videoURL)

            myFile.close()
    except:
        print("Error")


def startup():
    print(library.getUsername())  # Confirming the correct music library object is loaded


if __name__ == '__main__':
    startup()
    readFromFile()
    mainMenu()
