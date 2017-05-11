# WebApp-for-breast-cancer-detection
* A flask application for breast cancer detection (Under Development). The app can tell whether the breast mass is benign or     malignant. It uses the deep neural net classifier to find the pattern in the data.
* Link of the dataset : http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29
* The attributes in the sample are in the range (1-10). So,doctors will enter the values of attributes and clicking on the 
  compute button can tell whether it's benign or malignant.
* Video : https://www.youtube.com/watch?v=ulB_VYAcY5U  

### Requirements ###

* Python >=2.7 or >=3.4
* TensorFlow >= 1.0.0
* Flask
* Heroku


### How to run ###

* $ pip install -r requirements.txt
* $ gunicorn controller:app --log-file=-
   

### Deploy to Heroku ###

* $ heroku apps:create [NAME]
* $ git add .
* $ git commit -m "first commit"
* $ git push heroku master


or Heroku Button

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
