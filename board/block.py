class Block():
    def __init__(self,number,owned) -> None:
        self.owned = owned
        self.number = number
        # self.is_special = special
    
    def block_data(self):
        print(self.number)
        print(self.owned)