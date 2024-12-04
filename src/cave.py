class cave:
    #This creates and intialises a cave object if level isn't entered it begins at 0
    def __init__(self, caveName, caveType, level = 0):
        self._caveName = caveName
        self._caveType = caveType
        self._level = level
    
    #Just prints the default statement where player is to be used when they enter a cave
    def __repr__(self):
        return f"Player has entered: {self._caveName} and it's a {self._caveType} themed cave\nStaring on Floor: {self._level}"
    
    #Caves has multiple floors, when new floor entered player is told.
    def caveDepth(self, level):
        if level > self._level:
            self._level = level
            return f"Player has moved up to Floor {level}"
            
        elif level < self._level:
            self._level = level
            return f"Player has moved down to Floor {level}"
            
        else:
            return f"Player is currently still on Floor {level}"