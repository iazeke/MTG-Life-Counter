import MTG_Life_Counter_Functions as mtg
pl_index = 3
player_num = mtg.startup()
players = mtg.player_names(player_num)
life = mtg.setup(player_num)
running = True
while running == True:
    mtg.request_query(players, life)
    for i in range(len(players)):
        print(f'{mtg.lf(players[i])} has {mtg.lf(life[i])} life ')