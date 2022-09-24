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

class Rockband(Band):
    def __init__(self, bandname, genre = "Rock", rock_concert_movements = ["Basic headbob", "One armed fist pump", "Jumping"]):
        Band.__init__(self, bandname, genre, home_awards = 0, international_award = 0)
        self.rock_concert_movements = rock_concert_movements
        
    def display_movements(self):
        print(self.rock_concert_movements)

class Choir(Band):
    def __init__(self, bandname, genre = "Choir"):
        Band.__init__(self, bandname, genre, home_awards = 0, international_award = 0)
        
band = Band("Sabaton", "Metal")

RockBand = Rockband("Queen")
print(RockBand.bandname, RockBand.genre)
RockBand.display_movements()

print("\n")
choir = Choir("idk")
print(choir.bandname, choir.genre)