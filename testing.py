from model import model, svm_model
from predict_cancer import new_prediction
import numpy as np

test_data = np.array([1.799e+01, 1.038e+01, 1.228e+02, 1.001e+03, 1.184e-01, 2.776e-01,
                      3.001e-01, 1.471e-01, 2.419e-01, 7.871e-02, 1.095e+00, 9.053e-01,
                      8.589e+00, 1.534e+02, 6.399e-03, 4.904e-02, 5.373e-02, 1.587e-02,
                      3.003e-02, 6.193e-03, 2.538e+01, 1.733e+01, 1.846e+02, 2.019e+03,
                      1.622e-01, 6.656e-01, 7.119e-01, 2.654e-01, 4.601e-01, 1.189e-01])


def start_test():
    user_test = input("Are we running a prediction based on new data or the test data? ['test', or 'new']: ")

    while user_test.lower() != 'quit' or user_test.lower() != 'test' or user_test.lower() != 'new':
        if user_test.lower() == 'quit':
            return "**No Test Performed**"
            break
        if user_test.lower() == 'test':
            prediction = new_prediction.prediction(svm_model, test_data)
            return prediction
            break
        elif user_test.lower() == 'new':
            prediction = new_prediction.prediction(svm_model, new_prediction.tumor_data())
            return prediction
            break
        else:
            print("Must enter 'test' or 'new', no quotes. Enter quit to exit.")