class Band:
    def __init__(self, bandname, genre, home_awards = 0, international_award = 0):
        self.bandname = bandname
        self.genre = genre
        self.home_awards = home_awards
        self.international_award = international_award
        
    def describe_band(self):
        print("The band is called", self.bandname, "and makes", self.genre, "music")

band = Band("Sabaton", "Metal")

print(band.bandname, band.home_awards, band.international_award)

band.home_awards = 6
band.international_award = 5

print("\n")
print(band.bandname, band.home_awards, band.international_award)