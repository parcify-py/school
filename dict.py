def atack(player1=str,player2=str):
    global characters
    if characters['player1']['shield'] > 0:
        characters['player1']['shield'] -= 1
        print(f"{player1.capitalize()} miss atack.")
    else:
        characters[player1]['hp'] -= characters[player2]['damage']
        print(f"{player2.capitalize()} atack {player1}\n ")

def print_hp():
    print(f"Player one hp: {characters['player1']['hp']} Player two hp: {characters['player2']['hp']} \n")

def superpower(player):
    if characters[player]['superpower'] == 'heal':
        characters[player]['hp'] += 50
    elif characters[player]['superpower'] == 'extra_damage':
        characters[player]['damage'] += 20
    
    

characters = {'player1':{'hp':100,'damage':20,'superpower':'heal','shield':2},'player2':{'hp':120,'damage':15,'superpower':'extra_damage','shield':1}}


print_hp()
atack('player1','player2')

atack('player1','player2')
atack('player1','player2')
print_hp()
superpower('player1')
print_hp()
superpower('player2')
atack('player1','player2')
print_hp()
