#!/usr/bin/python

import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("./compare/score.csv")

algos = set(data.algo)
for algo in algos:
    for dataset in set(data.dataset):
        csv_algo_dataset = data[data['dataset'] == dataset & data['algo'] == algo]

        accuracies = csv_algo_dataset['acc'].values.tolist()
        kfold = csv_algo_dataset['k_fold'].values.tolist()

        accs = [0,0,0,0,0]
        howmany = [0,0,0,0,0]

        for i, acc in enumerate(accuracies):
            accs[ (kfold[i] - 1) % 5 ] += acc
            howmany[ (kfold[i] - 1) % 5 ] += 1

        if 0 not in howmany:
            res = [i / j for i, j in zip(accs, howmany)]
            plt.scatter([1,2,3,4,5], accs, label=dataset)

    plt.title(algo)
    plt.xlabel("k-fold")
    plt.ylabel("acc")
    plt.ylim(0,1)
    plt.legend(bbox_to_anchor=(1.025, 1), loc='upper left', borderaxespad=0)
    plt.savefig(algo, bbox_inches='tight')
    plt.close()
