#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import umap

sns.set(style='white', context='notebook', rc={'figure.figsize':(14,10)})
reducer = umap.UMAP()

clf = svm.SVC(gamma = 0.001, C=100.)
iris = datasets.load_iris()
digits = datasets.load_digits()

clf.fit(digits.data[:-1], digits.target[:-1])

def main():
    pred = clf.predict(digits.data[-1:])
    print(pred)
    return pred

if __name__ == '__main__':
    main()
