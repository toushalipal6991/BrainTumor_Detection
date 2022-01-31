import numpy as np
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from flask import Flask,redirect, url_for, request, render_template


import flask
app = Flask(__name__)

best = load_model("save_model4.h5")


###################################################
#Adding image pre-processing function
def predict_tumor(img_path):
    print("entered predict tumor")
    # load the image
    img = load_img(img_path, target_size=(224, 224))  #(224,224,3)
    # convert to array
    img = img_to_array(img) #(224,224,3)
    # add batch size as a dimension 
    img = np.expand_dims(img, axis=0)  #(1,224,224,3)
    if best.predict(img)[0][0]>0.45:  # just a threshold
        return "This MRI scan indicates presence of Brain tumor"
    else:
        return "This is a Healthy Brain"

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