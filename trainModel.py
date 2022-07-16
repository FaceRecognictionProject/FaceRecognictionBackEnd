import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from joblib import dump, load
from pathlib import Path

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


INPUT_IMAGE_PATH = './Datasets/facesData'
OUTPUT_CSV_FILE = './Datasets/faces.csv'
PROCESSED_IMAGE_PATH = './Datasets/processed'
PROCESSED_CSV_FILE = './Datasets/processed.csv'
DETECTED_FACE_PATH = './Datasets/cropped'
DETECTED_CSV_FILE = './Datasets/cropped.csv'
OUTPUT_MODEL_NAME = './model1/ModelFaces.lib'
train_csv_file = PROCESSED_CSV_FILE

def train_model(train_csv, output_model_name):
    dataset = pd.read_csv(train_csv, sep=',')
    ids = dataset.values[:,0]
    names = dataset.values[:,1]
    labels = dataset.values[:,2]

    images = []
    print('Training recognition model ...')
    i= 0 
    for item in names:
        i=i+1
        image = cv2.imread(str(item), 0)
        resizeds = cv2.resize(image, (200,200), interpolation=cv2.INTER_LINEAR)
        imgs = image[20:180,1:200]
        resized = cv2.resize(image, (90,90), interpolation=cv2.INTER_LINEAR)
        images.append(np.ravel(resized))
        #cv2.imshow("face",resized)
        #cv2.waitKey(0)
        print(i)

    clf = SVC(kernel='linear', probability=True)
    clf.fit(images, labels)
    dump(clf, output_model_name)
    print('Model created in', output_model_name)
    input("Press [ENTER] key to continue...")

train_model(train_csv_file, OUTPUT_MODEL_NAME)
