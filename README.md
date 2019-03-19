# Linear Classifier or discriminant based on perception algorithm.
Machine Learning Assignment

The purpose of Discriminant Analysis is to classify objects into one of two or more groups based on a set of features that
describe the objects. For example, we want to know whether a soap product is good or bad based on several measurements on
the product such as weight, volume, smell, etc. The object here is soap. The class category or the group (“good” and “bad”) is
what we are looking for (it is also called dependent variable). Each measurement on the product is called features that describe
the object (it is also called independent variable). If we can assume that the groups are linearly separable, we can use linear
discriminant model to classify object based on their features.

***Problem:***
A medical company tested two medicines say A and B to know the effectiveness of medicines to cure certain type
of influenza. Medicine A is given to 200 populations for observation and classified as class 1 category. Medicine B is given to
other 200 population and classified as class 2 category. The features selected to classify the medicines are side effect of
medicines and progress on cure. These features are scaled in positive and negative values. For example positive value of side
effect means common side effect and negative value of side effect means uncommon side effect. Similarly positive value of
progress on cure means recovery is in progress. Negative value indicates no progress on recovery.


****Question 1:****
Load medical data. The medical data consists three columns, the first column is side effect of medicine in terms of value. The
second column is recovery data in terms of value. The last column is class type.There are 400 observations and each row is
one observation or sample.
Plot the features for the medicine A and B and label the axes.


****Question 2:****
Implement in any programming language of your choice to Classify the medical data by using perceptron algorithm as described above.


## Hints:
Follow the following steps:
1. Find the data size (training data). Matlab command :size
2. Create initial weight vector as per the general equation described above.Matlab command:e.g
weight=ones(sizedata+1,1) , here we have to add constant .
3. Initialize test class data . It should be the same size as the data. Matlab command:Zeros
4. Create initial error vector. Matlab command : ones(1,number of iteration).
5. Make training data including class labels. (Initialize class level creating by using ones command) Matlab command:
6. Evaluate each sample in the training data(value=weight’*traindata)
7. Assign samples to classes(testclass(values>=0)=1 else 2)
8. Find incorrectly classified data(delta=trainclass-testclass)
9. Pick up indices , where error occurs(error=find(delta not equal to zero))
10. If no error stop
11. Compute correction term
12. Set learning rate.For example Rho=.005
13. Update weight vector.example weight=weight-rho*correction
14. Plot data according to sample class
15. Plot decision line according to equation as mentioned above.
