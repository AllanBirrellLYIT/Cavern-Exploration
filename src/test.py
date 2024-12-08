import pytest
from cave import Cave

def test_cave_default_init():
    """Test if the default initialisation of Cave works"""
    caves = Cave("Temple","Fire")
    assert caves.cave_name == "Temple" and caves.cave_type == "Fire" and caves.level == 0

def test_cave_init():
    """Test if the initialisation of Cave works with the value of floor"""
    caves = Cave("Tomb","Aztec",4)
    assert caves.cave_name == "Tomb" and caves.cave_type == "Aztec" and caves.level == 4
    
def test_cave_repr():
    """Test if the string representation of Cave works"""
    caves = Cave("a","b")
    assert f"{caves}" == "Player has entered: a and it's a b themed cave\nStarting on Floor: 0"

def test_cave_depth():
    """Test if the messages changes based on the Cave level"""
    caves = Cave("a","f",3)
    assert Cave.cave_depth(caves,4) == "Player has moved up to Floor 4"