class Song(object):
    def __init__(self, name, group, year, genre, playlist):
        self.__tuneName = name
        self.__tuneGroup = group
        self.__tuneYear = year
        self.__tuneGenre = genre
        self.__tunePlaylist = playlist

    def getTuneName(self):
        return self.__tuneName

    def getTuneGroup(self):
        return self.__tuneGroup

    def getTuneYear(self):
        return self.__tuneYear

    def getTuneGenre(self):
        return self.__tuneGenre

    def getTunePlaylist(self):
        return self.__tunePlaylist

    def toString(self):
        return self.__tuneName + " " + self.__tuneGroup + " " + self.__tuneYear + " " + self.__tuneGenre + " " + self.__tunePlaylist


    def txtString(self):
        return self.__tuneName + "," + self.__tuneGroup + "," + self.__tuneYear + "," + self.__tuneGenre + "," + self.__tunePlaylist