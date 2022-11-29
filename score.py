from sklearn.metrics import classification_report, confusion_matrix
import time
import logging
import matplotlib.pyplot as plt
from pathlib import Path

def result(algo,y_true,y_pred,time_ep,k_fold):
    epoch_time = int(time.time())
    logging.info("saving results ...")

    conf_matrix = confusion_matrix(y_true=y_true, y_pred=y_pred)
    
    #
    # Print the confusion matrix using Matplotlib
    #
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            ax.text(x=j, y=i,s=conf_matrix[i, j], va='center', ha='center', size='xx-large')

    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.savefig(str("compare/"+str(epoch_time)),dpi=300)
    plt.clf()

    report = classification_report(y_true=y_true, y_pred=y_pred,output_dict=True)
    names = ["algo", "k_fold", "time_running","time","acc"]
    acc = report["accuracy"]
    del report["accuracy"] 
    names += [ up +"_" + lo for up in report for lo in report[str(up)]]
    
    file_path = Path("compare/score.csv")
    if not file_path.is_file():
        with open(file_path,"a") as file:
            file.write(",".join(names)+"\n")
    with open(file_path,"a") as file:
        result = [algo, str(k_fold), str(epoch_time),str(time_ep),str(acc)]
        result += [ str(report[upper][lo]) for upper in report for lo in report[upper]]
        file.write(",".join(result)+"\n")