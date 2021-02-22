import joblib
import numpy as np
from sklearn import datasets, preprocessing
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from PIL import Image
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from os import path
from os import remove


# This class create the ML AI from the sklearn datasets number
class Ai:
    # Constructor
    def __init__(self) -> object:
        self.array = None
        self.image_data = None

        # Getting MNIST Data Base
        self.digits = fetch_openml('mnist_784')
        self.train_img, test_img, self.train_lbl, self.test_lbl = train_test_split(self.digits.data, self.digits.target,
                                                                                   test_size=1, random_state=0)

        # Some variables for the ML Process save
        hog_features = np.array(self.train_img, 'float64')
        self.preProcess = preprocessing.MaxAbsScaler().fit(hog_features)

        # Checking if the ML Process exists
        if path.exists("mlp.pkl") is False:
            # Creating the Multi Layers Perceptron Classifier
            self.mlp = MLPClassifier(hidden_layer_sizes=(200,), activation='logistic', alpha=1e-4,
                                     solver='sgd', tol=1e-4, random_state=2, max_iter=200,
                                     learning_rate_init=.0001, verbose=True)

            # Fitting data between images and its labels
            self.mlp.fit(self.train_img, self.train_lbl)

            # Saving the ML Process in .pkl file
            joblib.dump((self.mlp, self.preProcess), "mlp.pkl", compress=3)

        else:
            # Loading existing ML Process
            self.mlp, self.preProcess = joblib.load("mlp.pkl")

    # Method that returns the predicted digit from an image
    def predict(self, image, is_image: bool) -> int:
        # is_image is a bool that tells us if the transferred image is an file or an array
        if is_image is True:
            self.passing_image_to_array(image)
        else:
            self.image_data = image

        # Passing the image data in the first case of the images to be predicted
        self.train_img[0] = self.image_data

        # Predicting the digit
        prediction = self.mlp.predict(self.train_img)

        # To print the accuracy_score of our ML Process you can remove the comment just below
        # print(accuracy_score(self.train_lbl, prediction))

        # Returning the prediction
        return int(prediction[0])

    # Function that passes the image into an image fitting with the MNIST DB image's size
    def passing_image_to_array(self, image) -> None:
        # Passing the image in grey scale
        self.image_data = np.array(Image.open(image).convert('L'))
        Image.fromarray(self.image_data).save("./assets/grey.png")

        # Resizing image to a 28*28 image
        self.image_data = np.array(Image.open("./assets/grey.png").resize((28, 28)))
        Image.fromarray(self.image_data).save("./assets/rescaled_image.jpg")

        # Passing the 2D image to a 1D array
        self.image_data = self.image_data.flatten()

        # Removing temporary files
        remove("./assets/grey.png")
        remove("./assets/rescaled_image.jpg")
