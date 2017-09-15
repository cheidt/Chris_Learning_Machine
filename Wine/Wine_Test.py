import pandas as pds
import matplotlib.pyplot as plt

class Wine():
  def __init__(self):
    self.Process()

  def Process(self):
    whit = pds.read_csv("winequality-white.csv", sep=";", header=0)
    reds = pds.read_csv("winequality-red.csv", sep=";", header=0)
    w_qual = whit.groupby("quality").mean()
    r_qual = reds.groupby("quality").mean()
    plt.show(plt.hist(whit["pH"], 100))
    plt.show(plt.hist2d(whit["quality"], whit["pH"], 100))

    # print whit["pH"]
    # face = pds.DataFrame.hist(whit["pH"])
    # face.show()
    # print(whit("pH"))
    # plt.hist()

if __name__ == "__main__":
  Wine()