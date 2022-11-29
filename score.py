from sklearn.metrics import classification_report, confusion_matrix

def result(algo,y_true,y_pred,time,k_fold):
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
    plt.save(str("compare/"+epoch_time))

    report = classification_report(y_true=y_true, y_pred=y_pred)

    names = ["algo", "k_fold", "time_running","time"]
    names += [ upper +"_" + lo for upper in report for lo in report[upper]]
    
    file_path = Path("compare/score.csv")
    if not file_path.is_file():
        with open(file_path,"a") as file:
            file.write(",".join(names)"\n")
    with open(file_path,"a") as file:
        result = [algo, k_fold, epoch_time,time]
        result += [ report[upper][lo] for upper in report for lo in report[upper]]
        file.write(",".join(result)"\n")
            

