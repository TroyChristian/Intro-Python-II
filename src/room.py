
from player import Player 
class Room():
    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None 
        self.e_to = None
        self.w_to = None

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f'{direction}_to')
        return None 
    