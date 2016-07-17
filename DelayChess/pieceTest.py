from piece import Piece
from textColors import bcolors as bc
pawn = Piece("pawn", "p", [0,1], (2,1), bc.OKBLUE)
horse = Piece("horse", "h", [1,2], (1,1), bc.OKGREEN)
print pawn
print horse
