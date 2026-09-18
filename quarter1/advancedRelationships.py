# === PARENT CLASS ===
class Melody:
    def __init__(self, title, creator, length, liked):
        self.title = title #public
        self.creator = creator #public
        self.length = length #public
        self.__liked = liked #private
    def playMelody(self):
        minutes = self.length // 60
        seconds = self.length % 60
        return f"▶︎ Now playing: '{self.title}' by {self.creator} ({minutes}:{seconds:02d})"
    def setLike(self, status: bool):
        if isinstance(status, bool):
            self.__liked = status
            return "✓ Like status updated"
        return "✖ Invalid value. Must be True or False."
    def printDetails(self):
        minutes = self.length // 60
        seconds = self.length % 60
        heart = "❤︎⁠ Liked" if self.__liked else "♡ Not liked"
        return f"Title : {self.title}\nCreator: {self.creator}\nDuration: {minutes}:{seconds:02d}\nStatus: {heart}"
    def getLiked(self):
        return self.__liked
    
# === CHILD CLASS ===
class Song(Melody):
    def __init__(self, title, creator, length, liked, album, releaseYear):
        super().__init__(title, creator, length, liked)
        self.album = album
        self.releaseYear = releaseYear
    def getAlbum(self):
        return self.album
    def getYear(self):
        return self.releaseYear
    def printDetails(self):
        base = super().printDetails()
        return f"{base} | Album: {self.album} ({self.releaseYear})"

# === COMPOSITION CLASS ===
class MusicCollection:
    def __init__(self):
        self.__melodyList = [] #It owns the melodies
    def addMelody(self, melody):
            self.__melodyList.append(melody)
    def showAll(self):
        if not self.__melodyList:
            return "There are no melodies saved yet.\n"
        output = "\nSaved Melodies:\n"
        output += "-" * 30 + "\n"
        for melody in self.__melodyList:
            output += melody.printDetails() + "\n"
            output += "-" * 30 + "\n"
        return output

# === EXAMPLE ===
if __name__ == "__main__":
    collection = MusicCollection()
    song1 = Song("HOT TO GO!", "Chappell Roan", 185, False, "The Rise and Fall of a Midwest Princess", 2023)
    melody1 = Melody("Fresh Eyes", "Andy Grammar", 198, True)
    song2 = Song("Loser of the Year", "Simple Plan", 206, True, "Get Your Heart On!", 2011)
    collection.addMelody(song1)
    collection.addMelody(melody1)
    collection.addMelody(song2)
    print(collection.showAll())