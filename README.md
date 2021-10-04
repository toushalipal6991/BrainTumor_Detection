# :stethoscope: :drop_of_blood: Detection of Brain Tumor Based on MRI scan images of Brain
## :cinema: Demo :point_down::-

![Demo](https://github.com/toushalipal6991/BrainTumor_Detection/blob/master/BrainTumorDetection%20-%20Copy.gif)

## Aim of this Project:-
This project aims to detect Brain tumor as and when the Deep Learning model (CNN has been extensively used) is fed with MRI scan images of brains of different patients.

## Datasets:-
- Training Dataset :arrow_right: [Edureka](https://www.youtube.com/watch?v=7MceDfpnP8k)
- Testing images after deployment :arrow_right: [Kaggle](https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection)

## HLD(High Level Design)
- Train-CrossValidation-Test split :arrow_right: Entire dataset was split into 80(train + cross validation):20(test) ratio.
- Pre-processing the data :arrow_right: All images were divided into Standard Directories so as to be able to use the [Keras ImageDataGenerator class](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)
for Image Augmentation.
- Choosing Model Architectures :arrow_right: 4 different CNN archiectures were used. 
- Each of these models were fed with a completely unseen Test set of images and final accuracy was determined on the basis of prediction accuracy.
- Below table respresents each CNN architecture used and their test accuracies:-
![Table]()
