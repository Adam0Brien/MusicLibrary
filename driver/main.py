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
    print("1) Add a Song")
    print("2) List all Songs")
    print("3) Search song by name")
    print("4) List all songs of a certain genre")
    print("-----------------")
    print("5) Read in data from txt file")
    print("6) Search for song on Youtube")
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
        readFromFile()
    if option == 6:
        searchYoutube()
    if option == 10:
        exit()
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
def addPlaylist():
    playlistName = input("Playlist name: ")

    newPlaylist = MyMusicLibrary.MyMusicLibrary.addPlaylist(playlistName, songsList)

    mainMenu()


# TODO
def addSongToPlaylist():
    mainMenu()


def listSongs():
    for song in allSongsList:
        print(song.toString())


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


def deleteSongFromPlaylist():
    print("delete a song from a playlist")


def readFromFile():
    fname = input("Enter the name of the file you wish to open for reading: ")

    try:
        with open(fname, 'r') as myFile:
            for line in myFile:
                sName, sGroup, sYear, sGenre, sPlaylist = line.split(',')

                newSong = Song.Song(sName, sGroup, sYear, sGenre, sPlaylist)
                print(newSong.toString())
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

                if songName in line.casefold(): #casefold ignores case sensitivity
                    found = 1
                    break

            if found == 0:
                print("")
                print('Song Name ', songName, ' not found in file, You cant search if you haven\'t added the song')
                print("")
                mainMenu()
            else:
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + songName.replace(" ", ""))
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
