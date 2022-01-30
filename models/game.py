class Game():
    
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def get_winner(self, player_one, player_two):
        if player_one.option == "rock" and player_two.option == "scissors":
            return player_one
        if player_one.option == "scissors" and player_two.option == "paper":
            return player_one
        if player_one.option == "paper" and player_two.option == "rock":
            return player_one
        if player_one.option == "scissors" and player_two.option == "rock":
            return player_two
        if player_one.option == "paper" and player_two.option == "scissors":
            return player_two
        if player_one.option == "rock" and player_two.option == "paper":
            return player_two
        if player_one.option == player_two.option:
            return None

    def display_winner(self, winner):
        if winner == None:
            return "No winner, this game was a draw!"
        else:
            return f"{winner.name} wins the game!"