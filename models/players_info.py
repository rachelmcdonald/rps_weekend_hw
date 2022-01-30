from models.player import Player
from models.game import *

player_one = Player("Player One", "Rock", "Paper", "Scissors")
player_two = Player("Player Two", "Rock", "Paper", "Scissors")
players = [player_one, player_two]

def add_player_choice(player):
    players.append(player)