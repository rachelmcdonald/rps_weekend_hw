from flask import render_template
from app import app
from models.players_info import players
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<option_one>/<option_two>')
def display_winner(option_one, option_two):
    player_one = Player("Player One", option_one)
    player_two = Player("Player Two", option_two)
    winner = Game.get_winner(player_one, player_two)
    Game.display_winner(winner)
    return render_template('index.html', player_one, player_two)