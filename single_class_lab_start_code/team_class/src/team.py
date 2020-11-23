class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0



    def add_player(self, new_player_name):
        self.players.append(new_player_name)


    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
        else:               # need to reduce indentation on this line, otherwise only the first player is checked
            return False

    def play_game(self, victory):
        if victory == True:
            self.points += 3


    
    