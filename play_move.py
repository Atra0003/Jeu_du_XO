from board import BOARD

class PlayMove:
    def __init__(self, board):
        self.__board = board
        self.__position = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
        self.__nb_case = 9
        self.__cpt = 0
        
    def placement(self):
        cheking = True
        signe_player = self.player()
        while cheking == True:
            place = int(input("entrer une val : "))
            tup = self.__position[place]
            cheking = self.verifie_case(tup)
            
        self.__board.set_board(tup, signe_player)
        self.__board.affiche_board()
        
    def player(self):
        if self.__cpt % 2 == 0:
            signe = "X"
        else:
            signe = "O"
        self.__cpt += 1
        return signe

    def verifie_case(self, tup):
        if self.__board.affiche_place(tup) != ".":
            occupe = True
        else:
            occupe = False
        return occupe
            
    

if __name__ == "__main__":
    TAILLE_PLATAEU = 3
    pm = PlayMove(TAILLE_PLATAEU)
    


