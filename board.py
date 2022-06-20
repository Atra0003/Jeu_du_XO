


class BOARD:
    def __init__(self, taille):
        self.__t_board = taille
        self.__board = []
        self.__affiche = ""
        
    def build_board(self):
        for i in range(self.__t_board):
            elem = []
            for j in range(self.__t_board):
                elem.append(".")
            self.__board.append(elem)
        return self.__board
    
    def affiche_board(self):
        print(" " + " -"*self.__t_board)
        for i in range(self.__t_board):
            print("|", end=" ")
            for j in range(self.__t_board):
                char = self.affiche_place((i, j))
                print(char, end=" ")
            print("|")
        print(" " + " -"*self.__t_board)
    
    def affiche_place(self, place):
        return self.__board[place[0]][place[1]]
    
    def set_board(self, place, modif):
        self.__board[place[0]][place[1]] = modif
        
    def M_board(self):
        return self.__board
        
if __name__ == "__main__":
    TAILLE_PLATAEU = 3
    M = BOARD(TAILLE_PLATAEU)
    M.build_board()
    M.set_board((0, 0), "#")
    M.set_board((2, 2), "#")
    M.affiche_board()
    #print(M.M_board())

