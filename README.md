# MachineLearning

https://www.overleaf.com/6277751678wbdzgcjpxcrf

### Introduction
Multi-instance (MI) classification is a subtype of supervised learning. Instead of working with
individually labelled data points (instances), we work with bags (sets of instances). Class
labels of bags are related to the instances within it using one of a range of possible
assumptions.

For instance, under the standard assumption we view any bag with a positively labelled
instance as positive itself. A good use case is the popular Musk dataset. This dataset
comprises features describing molecules, some of which are classified as musks (a class of
substances with a specific smell that have chemical properties useful in making a particular
type of drug). However, each of these molecules appear in different conformations (shapes),
which are pooled together. Therefore, a positive label is assigned to a set (bag) of all present
conformations of a given molecule based on at least one of the conformations being
classified as musk.

More elaborate assumptions include a looser threshold-based rule and assume a minimum
number of positive instances required for a positive bag class label, or the collective
assumption which views bags as probability distributions and lets us learn a classifier that
can tell whether an instance comes from a positive or negative bag.
Some MI learning algorithms label bags directly (eg. nearest-neighbour classifiers) while
others do so through learning a concept for labelling instances individually (eg. neural
networks adapted for a multi-instance setting).

An exciting use case for MI classification is image analysis. Taking patches (regions) of
images as bags, we can classify entire images based on learning instance-level
representations and combining them. Recent advances in MI learning include neural
networks with residual connections (similarly as in ResNet CNN networks for image
classification). Finally, the use of attention maps [1,2] can reveal which patches are
responsible for a given bag class label. As an alternative to convolutional neural networks,
this application holds promise in medical diagnostics due to good interpretability.

### Project scope

In this project, we ask you to study existing MI classification methods, up to the recent ones,
and to present a use case on real-world data (eg. for drug-activity prediction, text
categorisation or content-based image classification). Compare different classification
algorithms and their parameters. Include a multiple-instance neural network in your
comparison and evaluate its performance. We will appreciate if you explore the concept of
attention weights and interpretability in your model.

### Literature and software
There are numerous blog posts and lectures online that introduce multi-instance learning.
The lecture part of this workshop gives a nice overview of both older and more recent
concepts in the field.
Skimming through Carbonneau et al. (2018) gives a good idea of what issues one has to
tackle with different types of data (they have a GitHub repo as well, however they use
MATLAB).
Wang et al. (2018) give more information on MI neural networks, and provide TensorFlow
implementations.
Xiong et al. (2021) use data about T-cell receptors (structures active in the immune system)
for cancer detection, comparing various multi-instance learning techniques.
Datasets
Here are some examples. The Musk dataset has been seminal in the field, and you can start
off by testing your code on it. Similarly, for image data the MNIST handwritten digits dataset
or CIFAR-10 are classics.
In a next step, biomedical datasets like Skin Cancer MNIST: HAM1000 or chest X-ray
images for pneumonia detection could be interesting to you, since they present an
opportunity to use more advanced, deep-learning approaches to classification.
### References
[1] Ilse, Maximilian, Tomczak, Jakub M., and Welling, Max. "Attention-based Deep Multiple
Instance Learning". ICML. PMLR, 2018.
[2] Papadopoulos, Alexandros, Topouzis, Fotis, and Delopoulos, Anastasios. "An
interpretable multiple-instance approach for the detection of referable diabetic retinopathy in
fundus images". Nature Sci Rep, 2021.
[3] Carbonneau, Marc-André, et al. "Multiple instance learning: A survey of problem
characteristics and applications". Pattern Recognition 2018.
[4] Wang, Xinggang, et al. "Revisiting multiple instance neural networks". Pattern
Recognition, 2018.
[5] Xiong, Danyi, et al. "A comparative study of multiple instance learning methods for cancer
detection using T-cell receptor sequences". Computational and Structural Biotechnology
Journal, 2021.
