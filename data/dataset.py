from __future__ import absolute_import, print_function
from pathlib import Path
import pandas as pd
import os

class Dataset(object):
    
    def __init__(self,path,name):
        self.df = pd.read_csv(path)
        self.shape = self.df.shape[0]
        self.__attrb__ = {'name':name,
                          'size':self.df.size(),
                          'nrows':self.df.shape[0]}
    
    def preprocess(self,columns,size_limit=None):
        pass
    
    def plot_hist(self, columns, fig_size):
        pass

    def __repr__(self):
        attr = self.__attrb__
        return f'{attr[name]} Dataset of size {attr[size]} and {attr[nrows]}number of rows'
    
