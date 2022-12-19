#!/usr/bin/python

import pandas
import matplotlib.pyplot as plt

csvreader = pandas.read_csv("./compare/score.csv")

algos = ["MILboost LogSumExponential", "MILboost", "MissSVM", "sbMIL", "sbMIL", "SIL", "STK", "NSK", "MICA"]
for algo in algos:
    csv_algo = csvreader[csvreader['algo'] == algo]

    for dataset in ['fox','mutagenesis-atoms','mutagenesis-bonds','mutagenesis-chains','eastWest','elephant','tiger','westEast', 'musk1']:
        csv_algo_dataset = csv_algo[csv_algo['dataset'] == dataset]

        plt.scatter(csv_algo_dataset['k_fold'], csv_algo_dataset['acc'], label=dataset)

    plt.title(algo)
    plt.xlabel("k-fold")
    plt.ylabel("acc")
    plt.legend(bbox_to_anchor=(1.025, 1), loc='upper left', borderaxespad=0)
    plt.savefig(algo, bbox_inches='tight')
    plt.close()