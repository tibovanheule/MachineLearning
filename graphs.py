#!/usr/bin/python

import pandas
import matplotlib.pyplot as plt

csvreader = pandas.read_csv("./compare/score.csv")

csv_NSK = csvreader[csvreader['algo'] == "MILboost"]

for dataset in ['fox','mutagenesis-atoms','mutagenesis-bonds','mutagenesis-chains','eastWest','elephant','tiger','westEast', 'musk1']:
    csv_NSK_dataset = csv_NSK[csv_NSK['dataset'] == dataset]

    plt.scatter(csv_NSK_dataset['k_fold'], csv_NSK_dataset['acc'], label=dataset)

plt.title("MILBOOST")
plt.xlabel("k-fold")
plt.ylabel("acc")
plt.legend(bbox_to_anchor=(1.025, 1), loc='upper left', borderaxespad=0)
plt.show()

print(csv_NSK)