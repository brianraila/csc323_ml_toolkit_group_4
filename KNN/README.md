### KNN Algorithm

Implemented from scratch using Python (works both on 2 and 3)


###### Usage :

```
from knn import KNN

knn_inst = KNN()


# loadDataset('../datasets/iris.data', < split ratio >, < length of features >)

knn_inst.loadDataset('../datasets/iris.data', 0,67, 4)


# knn(< instance >, < value of k >)
knn_inst.knn([5.1,3.5,1.4,0.2], 3)

#Wait and see magic 

```


###### Enjoy

###### NOTE : Accuracy is between 91 - 98 %