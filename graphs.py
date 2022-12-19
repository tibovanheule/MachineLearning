#!/usr/bin/python

import pandas
import matplotlib.pyplot as plt

csvreader = pandas.read_csv("./compare/score.csv")

algos = ["MILboost LogSumExponential", "MILboost", "MissSVM", "sbMIL", "sbMIL", "SIL", "STK", "NSK", "MICA"]
for algo in algos:
    csv_algo = csvreader[csvreader['algo'] == algo]

    for dataset in ['fox','mutagenesis-atoms','mutagenesis-bonds','mutagenesis-chains','eastWest','elephant','tiger','westEast', 'musk1', 'musk2']:
        csv_algo_dataset = csv_algo[csv_algo['dataset'] == dataset]

        accuracies = csv_algo_dataset['acc'].values.tolist()
        kfold = csv_algo_dataset['k_fold'].values.tolist()

        accs = [0,0,0,0,0]
        howmany = [0,0,0,0,0]

        for i, acc in enumerate(accuracies):
            accs[ (kfold[i] - 1) % 5 ] += acc
            howmany[ (kfold[i] - 1) % 5 ] += 1

        if(not howmany.__contains__(0)):
            res = [i / j for i, j in zip(accs, howmany)]
            plt.scatter([1,2,3,4,5], accs, label=dataset)

    plt.title(algo)
    plt.xlabel("k-fold")
    plt.ylabel("acc")
    plt.ylim(0,1)
    plt.legend(bbox_to_anchor=(1.025, 1), loc='upper left', borderaxespad=0)
    plt.savefig(algo, bbox_inches='tight')
    plt.close()
