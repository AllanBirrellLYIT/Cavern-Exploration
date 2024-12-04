class cave:
    def __init__(self, caveName, caveType, level = 0):
        self._caveName = caveName
        self._caveType = caveType
        self._level = level
        
    def __repr__(self):
        return f"Player has entered: {self._caveName} and it's a {self._caveType} themed cave\nStaring on Floor: {self._level}"
    
    def caveDepth(self, level):
        if level > self._level:
            self._level = level
            return f"Player has moved up to Floor {level}"
            
        elif level < self._level:
            self._level = level
            return f"Player has moved down to Floor {level}"
            
        else:
            return f"Player is currently still on Floor {level}"