"""This class is to use and create a cave object"""
class Cave:
    """This creates and intialises a cave object, if the level isn't entered it begins at 0"""

    def __init__(self, cave_name, cave_type, level = 0):
        '''
        Returns the string for a Cave object

            Parameters:
                self (cave): An object of the class cave
                cave_name (str): String for the cave's name
                cave_type (str): String for the cave type
                level (int): Integer for the cave floor

            Returns:
                Object (cave): Creating the cave object
        '''
        self.cave_name = cave_name
        self.cave_type = cave_type
        self.level = level

    #Just prints the default statement where player is to be used when they enter a cave
    def __repr__(self):
        '''
        Returns the string for a Cave object

            Parameters:
                self (cave): An object of the class cave

            Returns:
                String (str): String representation of Cave
        '''
        return f"Player has entered: {self.cave_name} and \
it's a {self.cave_type} themed cave\nStarting on Floor: {self.level}"

    def cave_depth(self, level):
        '''
        Returns the string for a Cave object

            Parameters:
                self (cave): An object of the class cave
                level (int): A decimal interger representing the floor level

            Returns:
                String (str): Outputs the current floor to player their on with unique message
        '''
        if level > self.level:
            self.level = level
            return f"Player has moved up to Floor {level}"

        if level < self.level:
            self.level = level
            return f"Player has moved down to Floor {level}"

        return f"Player is currently still on Floor {level}"
