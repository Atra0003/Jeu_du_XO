


class WINNER:
    def __init__(self, board):
        self.__board = board
        self.__pos = [(0,0),(0,1),(1,0), (0,2)]
        self.__move = [(0, 1),(1,0),(1,1), (1,-1)]
        #self.veri = 0



    def win(self):
        for elem in self.__pos:
            if self.__board.affiche_place((elem[0],elem[1])) != ".":
                for i in self.__move:
                    L = []
                    if L == []:
                        L.append(elem)
                        contenu = self.__board.affiche_place((elem[0],elem[1]))
                    tupl = elem[0] + i[0], elem[1] + i[1]
                    for j in range(2):
                        ret = self.is_in_board(tupl)
                        if ret:
                            if self.__board.affiche_place((tupl[0],tupl[1])) == contenu:
                                L.append(tupl)
                                tupl = tupl[0] + i[0], tupl[1] + i[1]
                    if len(L) == 3:
                        first = L[0]
                        return self.__board.affiche_place((first[0],first[1]))
                            
                            
    def is_in_board(self, pos):
        pos_l = pos[0]
        pos_c = pos[1]
        if 0 <= pos_l < 3 and 0 <= pos_c < 3:
            return True
        else:
            False
    
    
    #######################"
    """
    def affiche_place(self, place):
        return self.board[place[0]][place[1]]
        
    """
    
    
if __name__ == "__main__":
    M = [["X", "O", "X"],["O", "X", "O"],["X", ".", "."]]
    #M = [[0,1,1],[1,1,3],[4,0,0]]
    #M = [[0,1,1],[1,1,3],[4,0,0]]
    W = WINNER(M)
    print(W.win())

