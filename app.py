import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os
import numpy as np
import pandas as pd
import random
import shutil
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
from tensorflow.keras.models import Sequential,Model,load_model
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
import math
import seaborn as sns
from tensorflow.keras.callbacks import Callback,ModelCheckpoint,EarlyStopping,ReduceLROnPlateau,LearningRateScheduler
from tensorflow.keras.applications.vgg16 import VGG16,preprocess_input
from prettytable import PrettyTable
from flask import Flask,redirect, url_for, request, render_template


import flask
app = Flask(__name__)

best = load_model("best_model.h5")


###################################################
#Adding image pre-processing function
def predict_tumor(img_path):
    print("entered predict tumor")
    # load the image
    img = load_img(img_path,target_size=(224,224))
    # convert to array
    img = img_to_array(img)/255
    img_array = np.array([img])
    # plt.imshow(img_array[0])
    # plt.show()
    # best = load_model("best_model.h5")
    if best.predict(img_array)[0][0]>0.45:
        return "This MRI scan indicates presence of Brain tumor"
    else:
        return "This is a Healthy Brain"
    # return best.predict(img_array)[0][0]
###################################################

@app.route('/', methods=['GET'])
def welcome():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        imagefile=request.files['imagefile']
        if imagefile:
            image_path = "./static/" + imagefile.filename
            imagefile.save(image_path)
            return render_template('index.html',prediction=predict_tumor(image_path),imageloc=imagefile.filename)
    return render_template('index.html',prediction=predict_tumor(image_path),imageloc = None)


if __name__ == "__main__":
	app.run(port=8080)


#References:-
#https://www.youtube.com/watch?v=0nr6TPKlrN0&ab_channel=Jay    