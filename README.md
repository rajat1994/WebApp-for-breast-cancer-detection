# WebApp-for-breast-cancer-detection
* A flask application for breast cancer detection (Under Development)
* Link of the dataset : http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29


### Requirement ###

* Python >=2.7 or >=3.4
* Scikit-learn


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
