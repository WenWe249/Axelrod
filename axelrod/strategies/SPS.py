from axelrod import player 

class schoolprojectstrat(player);

"""A player cooperate in 95% of the case independently of opponent's move """

name= 'strat'

classifier = {
'memory_depth': 0,
'stochastic': False,
'inspects_source': False,
'manipulates_source': False,
'manipulates_state': False
}


def schoolprojectstrat(self,opponent):
    # Simulating a prbability of 0.95 of cooperation 
    alea=rd.random()
    if alea<=0.95:
        return 'C'
    if alea>0.95:
        return 'D'
  
return 'SPS'
