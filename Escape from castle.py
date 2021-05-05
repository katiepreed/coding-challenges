# player moves around rooms within a castle
# in each room thwew are items for the player to collect and use to solve puzzles and get out of each room
# goal is tp get out of castle
# each toom is represented as a grid of columns and rows, with each location within the grid holding a room tile
# ech room tile could contain an itemfor player to examine and collect
# some tiles in each room contain a door to another room in the castle

# info about player:
# - name
# - health between 0 and 100
# - location (column, row)

# methods that player can do:
# - describe themselves
# - list contents of bag
# - pick up an item
# - use an item
# - move tp another location on the board : get input about steps up/down and left/right
# room is 10x10

class Player:
    def __init__(self, name):
        self.name = name
        # between 0 and 100
        self.health = 100
        self.location = [0,0]
        self.items = ["perfume"]

    def describe(self):
        print("my name is : ", self.name)
        print("my current health is: ", self.health)

    def contents(self):
        print("Items: ")
        for item in self.items:
            print("- ", item)

    def add_item(self,item):
        self.items.append(item)

    def use_item(self,item):
        self.items.remove(item)

    def move(self):
        # changes column
        col = input("left (-) or right(+): ")
        # changes row
        row = input("steps up(+) or down(-): ")

        new_col = self.location[0] + int(col)
        new_row = self.location[1] + int(row)

        if (new_col > 10 or new_col < 0) or (new_row > 10 or new_col < 0):
            print("not possible")
        else:
            self.location[0] = new_col
            self.location[1] = new_row

        print("location: ", self.location)

kate = Player("Kate")

while True:
    print("""
- describe: 1
- contents: 2
- move: 3
- break: 0
""")
    num = input("pick option: ")
    if num == "1":
        kate.describe()
    elif num == "2": 
        kate.contents()
    elif num == "3": 
        kate.move()
    else:
        break
        
        
# classes to include:
class Place():
    def __init__(self):
        self.Description = ""
        self.ID = self.North = self.East = self.South = self.West = self.Up = self.Down = 0

class Character():
    def __init__(self):
        self.Name = self.Description = ""
        self.ID = self.CurrentLocation = 0
        # added Health attribute to Character class
        self.Health = 10
        
class Item():
    def __init__(self):
        self.ID = self.Location = 0
        self.Description = self.Status = self.Name = self.Commands = self.Results = ""
