import HW4Solution as La
import scr.FigureSupport as Fig


myGame = La.SetOfGames(prob_head=0.5, n_games=1000)

print(myGame.get_maximum())
print(myGame.get_minimum())
print(myGame.get_set_rewards())
# plot the histogram
Fig.graph_histogram(
    observations=myGame.get_set_rewards(),
    title='Histogram of Rewards',
    x_label='Rewards',
    y_label='Count')
