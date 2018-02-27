import HW4Solution as La


myGame = La.SetOfGames(prob_head=0.5, n_games=1000)

print(myGame.get_loss())
proportion = myGame.get_loss()/1000
print(proportion)
