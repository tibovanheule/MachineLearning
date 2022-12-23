#!/usr/bin/python

import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("./compare/score.csv")

algos = set(data.algo)
print(algos)
for algo in algos:
    csv_algo = data[data['algo'] == algo]
    print(algo)
    for dataset in set(csv_algo.dataset):
        csv_algo_dataset = csv_algo[csv_algo['dataset'] == dataset]

        accuracies = csv_algo_dataset['acc'].values.tolist()
        kfold = csv_algo_dataset['k_fold'].values.tolist()

        accs = [0,0,0,0,0]
        howmany = [0,0,0,0,0]

        for i, acc in enumerate(accuracies):
            accs[ (kfold[i] - 1) % 5 ] += acc
            howmany[ (kfold[i] - 1) % 5 ] += 1

        if 0 not in howmany:
            res = [i / j for i, j in zip(accs, howmany)]
            plt.scatter([1,2,3,4,5], res, label=dataset)

    plt.title(algo)
    plt.xlabel("k-fold")
    plt.ylabel("acc")
    plt.ylim(0,1)
    plt.legend(bbox_to_anchor=(1.025, 1), loc='upper left', borderaxespad=0)
    plt.savefig(algo, bbox_inches='tight')
    plt.close()

datasets = set(data.dataset)

#make sure the colours are consistent between different graphs
algo_colour = {'MI-Net': 'blue', 'MICA': 'red', 'MISVM': 'green', 'MILboost LogSumExponential': 'pink', 'MissSVM': 'orange', 'SIL':'purple', 'STK':'grey', 'miSVM': 'yellow', 'NSK': 'black', 'MILboost GeneralizedMean': 'brown', 'mi-Net': 'lawngreen', 'sbMIL': 'mediumslateblue'}


for dataset in datasets:
    csv_dataset = data[data['dataset'] == dataset]

    for algo in set(csv_dataset.algo):
        csv_algo_dataset = csv_dataset[csv_dataset['algo'] == algo]

        times = csv_algo_dataset['time'].values.tolist()
        kfold = csv_algo_dataset['k_fold'].values.tolist()

        ts = [0,0,0,0,0]
        howmany = [0,0,0,0,0]

        for i, time in enumerate(times):
            ts[ (kfold[i] - 1) % 5 ] += time
            howmany[ (kfold[i] - 1) % 5 ] += 1

        res = [i / j if j != 0 else -1 for i, j in zip(ts, howmany)]
        plt.scatter(res, [1,2,3,4,5], label=algo, color=algo_colour[algo])

    plt.title(dataset)
    plt.xlabel("time (s)")
    plt.ylabel("K-fold")
    plt.legend(bbox_to_anchor=(1.025, 1), loc='upper left', borderaxespad=0)
    plt.savefig(dataset + "_speed-overview", bbox_inches='tight')
    plt.close()
