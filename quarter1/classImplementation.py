class Melody:
    #To initialize the attributes of the class
    def __init__(self, title, creator, length, liked):
        self.title = title #public
        self.creator = creator #public
        self.length = length #public
        self.__liked = liked #private
    #Method 1 - to play the melody
    def playMelody(self):
        """Simulate playing the melody"""
        minutes = self.length // 60
        seconds = self.length % 60
        return f"▶︎ Now playing: '{self.title}' by {self.creator} ({minutes}:{seconds:02d})"
    #Method 2 - to receive the parameter and change the state (like status of the melody)
    def setLike(self, status: bool):
        """Safely update private like status"""
        if isinstance(status, bool):
            self.__liked = status
            return "✓ Like status updated"
        return "✖ Invalid value. Must be True or False."
    #Method 3 - to return the info + reads private attribute
    def printDetails(self):
        """Return formatted string of all melody info"""
        minutes = self.length // 60
        seconds = self.length % 60
        heart = "❤︎⁠ Liked" if self.__liked else "♡ Not liked"
        return f"Title : {self.title}\nCreator: {self.creator}\nDuration: {minutes}:{seconds:02d}\nStatus: {heart}"
    #Helps to safely read private attribute
    def getLiked(self):
        return self.__liked
# ==== TEST RUN ====
if __name__ == "__main__":
    # To create 2 different melody objects
    melody1 = Melody("HOT TO GO!", "Chappell Roan", 198, False)
    melody2 = Melody("Fresh Eyes", "Andy Grammar", 213, True)
    print("==== BEFORE ====")
    print("\n♫ Melody 1:")
    print(melody1.printDetails())
    print("\n♫ Melody 2:")
    print(melody2.printDetails())
    #Update only Melody 1
    print("\nUpdating Melody 1's like status to True...")
    melody1.setLike(True)
    print("\n==== AFTER ====")
    print("\n♫ Melody 1:")
    print(melody1.printDetails())
    print("\n♫ Melody 2:")
    print(melody2.printDetails())