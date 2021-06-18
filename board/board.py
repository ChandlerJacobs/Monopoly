import board.block as block

class Board():
    def __init__(self,grid) -> None:
        self.grid = grid

    
    def board_init(self):
        board = []
        dict_of_board = {}
        self.board = [i for i in range(1,self.grid*4+1)]

        for i in self.board:
            unit = block.Block(i,False)
            board.append(unit)
        
        for i in board:
            i.block_data()


        
    
    

