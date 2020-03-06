from flask import Flask,jsonify
import datetime
import pickle
import numpy as np
from flask import request
app = Flask(__name__)
model = pickle.load(open('RandomForest.pkl', 'rb'))

@app.route("/",methods=['GET', 'POST'])
def hello_www():
   x = datetime.datetime.now()
   if request.args.get('lat')==None or request.args.get('lng')==None:
     return "pass lat and lng"
   if request.method == 'GET':
     lat=float(request.args.get('lat'))
     lng=float(request.args.get('lng'))
     print(lat)
     print(lng)
     month=x.strftime("%m")
     day=x.strftime("%d")
     hours=x.strftime("%H")
     mins=x.strftime("%M")
     to_cal=[[lat, lat,month,day,hours,mins]]
     to_cal = np.asarray(to_cal, dtype='float64')
     prediction =model.predict_proba(to_cal)
     print(prediction)
     return jsonify({"class":str(prediction[0][0])})
   
  
if __name__ == "__main__":
    app.run(debug=True)
