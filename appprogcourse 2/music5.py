class Band:
    def __init__(self, bandname, genre, home_awards = 0, international_award = 0):
        self.bandname = bandname
        self.genre = genre
        self.home_awards = home_awards
        self.international_award = international_award
        
    def describe_band(self):
        print("The band is called", self.bandname, "and makes", self.genre, "music")

    def set_home_awards(self):
        print("Insert home awards of", self.bandname)
        self.home_awards = int(input())
        
    def set_international_awards(self):
        print("Insert international awards of", self.bandname)
        self.international_awards = int(input())

band = Band("Sabaton", "Metal")

print(band.bandname, band.home_awards, band.international_award)

band.set_home_awards()
band.set_international_awards()

print("\n")
print(band.bandname, band.home_awards, band.international_awards)