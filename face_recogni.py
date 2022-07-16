import cv2
import numpy as np
from joblib import load
from sklearn.svm import SVC
import json

def face_recogintion(recogni):

    HAAR_MODEL = 'haarcascade_frontalface_default.xml'
    SVM_MODEL = 'model1/ModelFaces.lib'

    font = cv2.FONT_HERSHEY_SIMPLEX
    color_known = (255,0,0)
    color_unknown = (200,200,200)
    threshold = 0.5

    detector = cv2.CascadeClassifier(HAAR_MODEL)
    classifier = load(SVM_MODEL)

    dimensions = recogni.shape
    img_resize_factor = 400 / dimensions[1] 

    facerecogni = cv2.resize(recogni, None,fx=img_resize_factor,fy=img_resize_factor,interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(facerecogni, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(
        gray, scaleFactor = 1.3, 
        minNeighbors = 5, 
        minSize = (50, 50))

    for (x, y, w, h) in faces:
        testset = []
        face = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face,(90,90),interpolation=cv2.INTER_LINEAR)
        testset.append(np.ravel(face_resized))

        pred = str(classifier.predict(testset))
        prob = classifier.predict_proba(testset)
        max_prob = max(prob[0])

        if max_prob >= threshold:
            text = ''.join(pred + ' (' + '{0:.2g}'.format(max_prob * 100) + '%)')        
            color = color_known
            cv2.putText(facerecogni, text, (x,y-10), font, 0.6, color, thickness=2)
        else:
            color = color_unknown
            cv2.putText(facerecogni, "Unknown", (x,y-10), font, 0.6, color,thickness=2)
            pred = "['Unknow']"

        cv2.rectangle(facerecogni, (x,y), (x+w,y+h), color, 2)

        de_face = pred[2:len(pred)-2]
        facedata = {  
            "IDname": "Unknow",
            "name": "",
            "lastname": "",
            "age": "",              
        }
        with open('Jsondata.json') as data:
            Datajson = json.load(data)
            DataPerple = Datajson['Perplejson']
            for jsonfile in DataPerple:
                if (de_face == jsonfile['IDname']):
                    facedata = {  
                        "IDname": jsonfile["IDname"],
                        "name": jsonfile["name"],
                        "lastname": jsonfile["lastname"],
                        "age": jsonfile["age"], 
                        "prob": max_prob            
                    }
    cv2.imshow('Face Classifier', facerecogni)
    cv2.waitKey(0)
    return(facedata)                    
    #print(facedata)              

     

cv2.destroyAllWindows()