import random

coinfaces = []
class Coin:
    def __init__(self, sides = "Heads"):
        self.sides = sides
        
    def toss_coin():
        toss = random.randint(0, 1)
        if toss == 1:
            print("Heads")
            coinfaces.append("Heads")
            
        elif toss == 0:
            print("Tails")
            coinfaces.append("Tails")

x = 0
while x < 10:
    x += 1
    Coin.toss_coin()
print(coinfaces.count("Heads"), "amount of heads")
print(coinfaces.count("Tails"), "amount of tails")
coinfaces = []
print("\n")    

x = 0
while x < 20:
    x += 1
    Coin.toss_coin()
print(coinfaces.count("Heads"), "amount of heads")
print(coinfaces.count("Tails"), "amount of tails")
coinfaces = []
print("\n")    

x = 0
while x < 50:
    x += 1
    Coin.toss_coin()
print(coinfaces.count("Heads"), "amount of heads")
print(coinfaces.count("Tails"), "amount of tails")