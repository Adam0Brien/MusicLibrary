class MyMusicLibrary(object):

    def __init__(self, username, playlistList, allSongsList):
        self.__username = username
        self.__playlistList = playlistList
        self.__allSongsList = allSongsList

    def getUsername(self):
        return self.__username

    def getPlaylistList(self):
        return self.__playlistList

    def getAllSongsList(self):
        return self.__allSongsList

    def addPlaylist(self, playlist):
        self.__playlistList.append(playlist)

    def removePlaylist(self, playlist):
        self.__playlistList.append(playlist)
