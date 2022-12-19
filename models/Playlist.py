class Playlist(object):

    def __init__(self, playlistName, songsList):
        self.__playlistName = playlistName
        self.__songsList = songsList
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__songsList):
            raise StopIteration
        song = self.__songsList[self.__index]
        self.__index += 1
        return song


    def getPlaylistName(self):
        return self.__playlistName

    def getSongsList(self):
        return self.__songsList

    def addSong(self, song):
        self.__songsList.append(song)

    def removeSong(self, song):
        self.__songsList.pop(song)

