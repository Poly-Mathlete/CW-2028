from game2048.textual_2048 import *
import pytest 
import requests
import json


def mock_input_return(obj, value) -> str :
    """
    Fonction qui simule une entrée de l'utilisateur pour le test.
    """
    # on crée la simulation input
    def fake_input():
        return value
    
    obj.setattr("builtins.input", fake_input)
    
    

def test_read_player_command(obj):
    
    mock_input_return(obj ,'g')  
    result = read_player_command()
    assert result == 'g'







 