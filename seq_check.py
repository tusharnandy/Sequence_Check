import numpy as np
import pandas as pd
class Sequence:
    def __init__(self, file_path=None):
        if file_path:
            self.dataframe = pd.read_csv(file_path, header=None)
            self.dataframe.drop(columns=0,inplace=True)
            self.dataframe.drop(0,inplace=True)
            self.dataframe.columns = ['Original']
            self.dataframe.reset_index(drop=True)
            self.p = self.dataframe['Original'].tolist()

    def difference(self, array):
        reduced = []
        for i in range(len(array)-1):
          reduced.append(array[i+1] - array[i])
        return reduced

    def ratio(self, array):
        reduced = []
        for i in range(len(array)-1):
            reduced.append(array[i+1]/array[i])
        return reduced

    def generate(self):
        self.p_diff_1 = self.difference(self.p)
        self.p_diff_2 = self.difference(self.p_diff_1)
        self.p_ratio_1 = self.ratio(self.p)
        self.p_ratio_2 = self.ratio(self.p_ratio_1)

    def all_datasets(self):
        self.generate()
        d_1 = pd.DataFrame({"Diff_1":self.p_diff_1})
        d_2 = pd.DataFrame({"Diff_2":self.p_diff_2})
        r_1 = pd.DataFrame({"Ratio_1":self.p_ratio_1})
        r_2 = pd.DataFrame({"Ratio_2":self.p_ratio_2})

        df = pd.concat([self.dataframe,d_1,d_2,r_1,r_2],axis=1)

        for i in range(20):
          df['Original'][i] = df['Original'][i+1]
        df['Original'][20] = np.nan

        df.drop(20,inplace=True)
        return df

    def moving_averages(self, array):
      # for smoothening sequences with randomness
      n = int(len(array)*5/200)
      smoothened = []
      for i in range(len(array)):
        window = np.arange(-n,n+1)
        neighbors = []
        for p in window:
          if i+p >= 0 and i+p<len(array):
            neighbors.append(array[i+p])
        val = np.array(neighbors).mean()
        smoothened.append(val)

      return np.array(smoothened)

    def non_decreasing(self, array):
        if len(array)==0:
          return False
        elif len(array) == 1:
          return True
        else:
          prev = array[0]
          for curr in array[1:]:
            if curr<prev:
              return False
          return True
