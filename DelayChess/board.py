from piece import Piece
from textColors import bcolors as bc

class Board():
    def __init__(self):
        self.boardState =  [[0 for i in xrange(8)] for j in xrange(8)]
        pawnblue = Piece("pawn", "p", [0,1], bc.OKBLUE)
        pawngreen = Piece("pawn", "p", [0,1], bc.OKGREEN)
        for i in range(len(self.boardState[1])):
            self.set_Peice(pawnblue,(i,1))
            #self.boardState[1][i] = pawnblue
        for i in range(len(self.boardState[6])):
            self.set_Peice(pawngreen,(i,6))
            #self.boardState[6][i] = pawngreen

        rookblue = Piece("rook", "r", [0,1], bc.OKBLUE)
        rookgreen = Piece("rook", "r", [0,1], bc.OKGREEN)
        self.set_Peice(rookblue, (0,0))
        self.set_Peice(rookblue, (7,0))
        self.set_Peice(rookgreen, (0,7))
        self.set_Peice(rookgreen, (7,7))

        knightblue = Piece("horse", "h", [0,1], bc.OKBLUE)
        knightgreen = Piece("horse", "h", [0,1], bc.OKGREEN)
        self.set_Peice(knightblue ,(1,0))
        self.set_Peice(knightblue ,(6,0))
        self.set_Peice(knightgreen ,(1,7))
        self.set_Peice(knightgreen ,(6,7))

        bishopblue = Piece("bishop", "b", [0,1], bc.OKBLUE)
        bishopgreen = Piece("bishop", "b", [0,1], bc.OKGREEN)
        self.set_Peice(bishopblue ,(2,0))
        self.set_Peice(bishopblue ,(5,0))
        self.set_Peice(bishopgreen ,(2,7))
        self.set_Peice(bishopgreen ,(5,7))

        kingblue = Piece("king", "K", [0,1], bc.OKBLUE)
        kinggreen = Piece("king", "K", [0,1], bc.OKGREEN)
        self.set_Peice(kingblue ,(3,0))
        self.set_Peice(kinggreen ,(3,7))

        queenblue = Piece("queen", "Q", [0,1], bc.OKBLUE)
        queengreen = Piece("queen", "Q", [0,1], bc.OKGREEN)
        self.set_Peice(queenblue ,(4,0))
        self.set_Peice(queengreen ,(4,7))

    def __str__(self):
        returnString = ""
        for j in range(len(self.boardState)):
            row = self.boardState[j]
            for i in range(len(row)):
                piece = self.boardState[j][i]
                if (j+i)%2 == 0:
                    returnString += bc.UNDERLINE + str(piece) + bc.ENDC + "|"
                elif (j+i)%2 == 1:
                    returnString += bc.BOLD + str(piece) + bc.ENDC + "|"
            returnString += "\n"
        return returnString
    def set_Peice(self, piece, location):
        locationy = location[1]
        locationx = location[0]
        self.boardState[locationy][locationx] = piece

    def move_Peice(self, fromLocation, toLocation):
        fx = fromLocation[0]
        fy = fromLocation[1]
        tx = toLocation[0]
        ty = toLocation[1]
        pieceToMove = self.boardState[fy][fx]
        self.boardState[fy][fx] = 0
        self.boardState[ty][tx] = pieceToMove
