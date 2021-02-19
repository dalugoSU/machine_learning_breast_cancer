from dataset import breast_cancer_dataset

class MachineLearningModel:

    import numpy as np
    import sklearn
    from sklearn import svm
    from sklearn import metrics

    def __init__(self, dataset):
        self.dataset = dataset

    def view_dataset(self):
        return self.dataset['data']


    def number_of_arrays(self):
        return len(self.dataset['data'])


    def add_data(self, data):
        new_dataset = self.np.concatenate((self.dataset['data'], data.reshape(-1, 30)))
        self.dataset = new_dataset


    def svm_model(self):
        x = self.dataset.data
        y = self.dataset.target

        x_train, x_test, y_train, y_test = self.sklearn.model_selection.train_test_split(x, y, test_size=0.2)

        classification = self.svm.SVC(kernel="linear", C=2)
        classification.fit(x_train, y_train)

        y_prediction = classification.predict(x_test)
        prediction_accuracy = self.metrics.accuracy_score(y_prediction, y_test)

        print(f"Prediction Accuracy: {prediction_accuracy * 100:.0f}%")

        return classification


model = MachineLearningModel(breast_cancer_dataset)
svm_model = model.svm_model()