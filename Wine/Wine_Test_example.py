import pandas as pds
import matplotlib.pyplot as plt
import seaborn as sns # new shit
plt.ion() # new shit

class Wine():
  def __init__(self):
    self.Process()

  def Process(self):
    whit = pds.read_csv("winequality-white.csv", sep=";", header=0)
    reds = pds.read_csv("winequality-red.csv", sep=";", header=0)
    w_qual = whit.groupby("quality").mean()
    r_qual = reds.groupby("quality").mean()

    
    # arguments to subplots: 1: number of rows, 2: number of columns
    # fig = figure handle
    # ax = axes object
    fig, ax = plt.subplots(1,2, figsize=(8,4)) # new shit
    fig.suptitle('Some Cool Plots') # new shit
    ax[0].hist(whit['pH'], bins=100) # new shit
    ax[0].set_xlabel('pH') # new shit
    ax[0].set_ylabel('Counts') # new shit
    ax[0].set_title('Distribution of White Wine ph') # new shit

    # Violin plots are like box-and-whisker plots on steroids. They show
    # a numeric distribution (fit with kernel density estimation, which is
    # kind of like a histogram with infinite bins) conditioned on a categorical
    # distribution. Instead of seeing quartiles like with a box plot, you
    # see the actual data distribution.
    sns.violinplot(data=whit, x='quality', y='pH', ax=ax[1]) # new shit 
    plt.tight_layout() # fixes problems with axes / ticks running off margins
                       # some of the time...

    # this updates the figure which the global plt pointer is
    # pointing to. Fun fact, it can also be used to create
    # simple animations.
    plt.pause(0.1) # new shit

    # plt.show(plt.hist(whit["pH"], 100))
    # plt.show(plt.hist2d(whit["quality"], whit["pH"], 100))

    # print whit["pH"]
    # face = pds.DataFrame.hist(whit["pH"])
    # face.show()
    # print(whit("pH"))
    # plt.hist()

if __name__ == "__main__":
  Wine()
  input("Press enter to exit") # new shit
