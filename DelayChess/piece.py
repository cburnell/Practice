from textColors import bcolors
class Piece:
    def __init__(self, name, symbol , movelist, team):
        self.name = name
        self.symbol = symbol
        self.movelist = movelist
        self.team = team
    def __str__(self):
        return self.team + self.symbol + bcolors.ENDC
    def printStatus(self):
        strOut = team
        strOut += self.name + "\n"
        strOut += str(self.movelist) + "\n"
        strOut += bcolors.ENDC
        return strOut
