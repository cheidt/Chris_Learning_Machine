import pandas as pds
import matplotlib.pyplot as plt
import seaborn as sns # new shit
import math
# import numpy as np
plt.ion() # new shit

class Wine():
  def __init__(self):
    self.Process()

  def Process(self):
    whit    = pds.read_csv("winequality-white.csv", sep=";", header=0)
    reds    = pds.read_csv("winequality-red.csv", sep=";", header=0)

    # self.Plot_Parameter(whit, "White")
    # self.Plot_Parameter(reds, "Red")
    # self.Plot_Against_Quality(whit, "White")
    # self.Plot_Against_Quality(reds, "Red")
    # self.Plot_Against_Color(whit, reds)
    self.Find_Correlation(whit)
    self.Find_Correlation(reds)

  def Find_Correlation(self, data):
    result = data.corr()


  def Plot_Against_Color(self, white, red):
    nwhites = white.shape[0]; nreds   = red.shape[0]
    white_c = ["white"] * nwhites; red_c   = ["red"]   * nreds
    white['color'] = white_c; red['color'] = red_c
    total = white.append(red, ignore_index=True)

    parameters = list(total)
    nparameters = len(parameters)
    plt_rows = math.floor((nparameters - 1) / 3)
    if (nparameters - 1) % 3 > 0:
      plt_rows += 1
    fig, ax = plt.subplots(int(plt_rows), 3)
    fig.suptitle('Characteristics of Red and White Wine as a Function of Quality')
    for i in range(len(parameters)):
      title = parameters[i]
      if title == 'quality' or title == 'color':
        continue
      print(title)
      r = math.floor(i / 3);
      c = i % 3
      sns.violinplot(data=total, x='quality', y=title, hue='color', split=True, ax=[r, c])
      # ax[r, c].set_xlabel('quality')  # new shit
      # ax[r, c].set_ylabel(title)
    plt.tight_layout()


  def Plot_Against_Quality(self, data, color):
    parameters = list(data)
    nparameters = len(parameters)
    plt_rows = math.floor((nparameters - 1) / 3)
    if (nparameters - 1) % 3 > 0:
      plt_rows += 1
    fig, ax = plt.subplots(int(plt_rows), 3)
    fig.suptitle('Characteristics of {} Wine as a Function of Quality'.format(color))
    for i in range(len(parameters)):
      title = parameters[i]
      if title == 'quality':
        continue
      r = math.floor(i / 3);
      c = i % 3
      sns.violinplot(data=data, x='quality', y=title, ax=ax[r, c])
      ax[r, c].set_xlabel('quality')  # new shit
      ax[r, c].set_ylabel(title)
    plt.tight_layout()


  def Plot_Parameter(self, data, color):
    parameters  = list(data)
    nparameters = len(parameters)
    plt_rows = math.floor(nparameters/3)
    if nparameters%3 > 0:
      plt_rows += 1
    fig, ax = plt.subplots(int(plt_rows), 3)
    fig.suptitle('{} Wine Histograms'.format(color))
    for i in range(len(parameters)):
      title = parameters[i]
      r = math.floor(i/3); c = i%3
      if title == 'sulphates' or title == 'alcohol':
        bins = 50
      elif title == 'quality':
        bins = data['quality'].max(axis=0) - data['quality'].min(axis=0) + 1
      else:
        bins = 100
      ax[r, c].hist(data[title], bins=bins)
      ax[r, c].set_xlabel(title)  # new shit
      ax[r, c].set_ylabel('Counts')  # new shit
    plt.tight_layout()


if __name__ == "__main__":
  Wine()
  input("Press enter to exit")  # new shit