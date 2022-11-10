class Playlist(object):

    def __init__(self, playlistName, songsList):
        self.__playlistName = playlistName
        self.__songsList = songsList

    def getPlaylistName(self):
        return self.__playlistName

    def getSongsList(self):
        return self.__songsList

    def addSong(self, song):
        self.__songsList.append(song)

    def removeSong(self, song):
        self.__songsList.remove(song)
