# Introduction to classes. Classes are one of the fundamental building blocks
# of componentizing code or object oriented programming.


class Sports_Team:
    """ This returns a sports team object
    
    Attributes:
        Coaches Name
        Team Name 
        Team Location """
    def __init__(self, coach_name, team_name, team_location):
        self.coach_name = coach_name
        self.team_name = team_name
        self.team_location = team_location
    
    def __str__(self):
        return 'The '+self.team_name
    
    def set_coach(self,coach_name):
        self.coach_name = coach_name
        
class NBA_Team(Sports_Team):
    """ This returns a NBA Team object which is derived from Sports Team."""
    def __init__(self, coach_name, team_name, team_location):
        Sports_Team.__init__(self,coach_name, team_name, team_location)
        self.num_of_games_this_season = 0
        self.wins = 0
        self.losses = 0
        self.win_percentage = 0
        
    def set_wins(self,num_of_wins):
        self.wins = num_of_wins
    
    def set_losses(self,num_of_losses):
        self.losses = num_of_losses
    
    def num_of_games_this_season(self,games):
        self.num_of_games_this_season = games
    
    def get_win_percentage(self):
        
        if self.wins + self.losses >0:
            return self.wins / (self.wins +self.losses)
        else:
            return 'No wins or losses yet'

class NFL_Team(Sports_Team):
    """ This returns a NFL Team object which is derived from Sports Team.""" 
    def __init__(self, coach_name, team_name, team_location):
        Sports_Team.__init__(self,coach_name, team_name, team_location)
        self.passing_yards = 0
        self.rushing_yards = 0
        self.playoff_wins = 0
        
    def set_passing_yards(self,passing):
        self.passing_yards = passing
        
    def set_rushing_yards(self, rushing):
        self.rushing_yards = rushing
    
    def set_playoff_wins(self, playoff_wins):
        self.playoff_wins = playoff_wins




Patriots = NFL_Team(coach_name= 'Bellicheck', team_name= 'Patriots', team_location= 'New England')

print(Patriots.__str__())
Patriots.set_passing_yards(522)
Patriots.set_rushing_yards(899)
Patriots.set_playoff_wins(2)


print(Patriots.team_location)
print(Patriots.coach_name)
print(Patriots.rushing_yards)
print('\n')

Golden_State = NBA_Team(coach_name= 'Kerr', team_name= 'Golden State Warriors', team_location='Cali')

Golden_State.set_losses(2)
Golden_State.set_wins(30)

print(Golden_State.get_win_percentage())
print(type(Golden_State))
print(type(Patriots))








     
        
        
        