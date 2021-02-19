### machine_learning_breast_cancer
 
- using sklearn built a machine learning algorithm to predict cancer from sklearn's breast_cancer_dataset.
- built a model class to quickly view the dataset, add data to the dataset, and create a model based on the updated data of the dataset.
- build a cancer prediction class wich takes in the model from the model class, and takes in data. You can either input your own, or use a test_data array included in the testing.py file.
- run main.py to run program.

#### File info

- dataset.py => Contains the initial dataset loaded from sklearn "breast cancer dataset"
- model.py => contains the class that creates a support vector model or svm machine learning model using this dataset. Has functions to add data, view data and create the model
- predict_cancer.py => class that takes the model and data to make a prediction. Has function to collect data in case you want to use your own to test against the model.
- testing.py => Contains a test_data array to use with the model.
- main.py => Run this to run the entire program. Calls the start_test() function from testing.py

#### Required

- sklearn
- installation: pip install sklearn
