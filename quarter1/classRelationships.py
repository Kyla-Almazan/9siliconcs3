# ==== EXISTING CLASS ====
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

# ==== NEW CLASS ====
class MusicCollection:
    def __init__(self, name):
        self.name = name
        self.melodies = [] #to store Melody objects
    def addMelody(self, melody_item):
        #to store the whole object, not just data
        self.melodies.append(melody_item)
    def showAll(self):
        print(f"\n=== Collection: {self.name} ===")
        for song in self.melodies:
            print(song.printDetails())
            print("-" * 30)

# ==== CREATE OBJECTS ====
print("\n--- BEFORE RELATIONSHIP ---")
my_collection = MusicCollection("My Favorite Tracks")
melody1 = Melody("HOT TO GO!", "Chappell Roan", 185, False)
melody2 = Melody("Fresh Eyes", "Andy Grammar", 198, True)
melody3 = Melody("Loser of the Year", "Simple Plan", 206, True)
print()
print("Collection created but empty.")
print()
print(melody1.printDetails())
print()
print(melody2.printDetails())
print()
print(melody3.printDetails())

# === BUILD RELATIONSHIP ===
print("\n--- BUILDING RELATIONSHIP ---")
my_collection.addMelody(melody1)
my_collection.addMelody(melody2)
my_collection.addMelody(melody3)
print()
print("All melodies added to collection!")

# === ACCESS DATA THROUGH RELATIONSHIP ===
print("\n--- AFTER RELATIONSHIP ---")
my_collection.showAll()
print("\nDirect access through relationship:")
print(f"First song by: {my_collection.melodies[0].creator}")
print(f"Is it liked? {my_collection.melodies[0].getLiked()}")