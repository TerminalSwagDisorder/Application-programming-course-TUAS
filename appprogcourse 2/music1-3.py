class Band:
    def __init__(self, bandname, genre):
        self.bandname = bandname
        self.genre = genre
        
    def describe_band(self):
        print("The band is called", self.bandname, "and makes", self.genre, "music")
    
    def is_active(self):
        print(self.bandname, "is active")
        
band = Band("Evil Activities", "Hardcore")
band2 = Band("Sabaton", "Metal")
band3 = Band("Powerwolf", "Metal")

band.describe_band()
band.is_active()

print("\n")
band2.describe_band()
print("\n")
band3.describe_band()