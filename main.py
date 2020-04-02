from flask import Flask, render_template
from flask import request
from werkzeug.datastructures import ImmutableMultiDict
app = Flask(__name__)
import pickle

#open a file where you stored the pickled data
file = open('model.pkl','rb')
clf = pickle.load(file)
file.close()

@app.route('/',methods=["GET", "POST"] )
def hello_world():
    if request.method == "POST":
        mydict = request.form.to_dict(flat=False)
        print("________________________-")
        print(mydict['fever'][0])
        print("________________________-")
        # fever = mydict['fever']
        # age = mydict['age']
        # Pain = mydict['Pain']
        # runnyNose = mydict['runnyNose']
        # diffBreath = mydict['diffBreath']

        # # code for inference
        # inputFeatures = [fever, Pain, age, runnyNose, diffBreath]
        # infectionProb = clf.predict_proba([inputFeatures])[0][1] 
        # print(infectionProb) 
        return render_template('index.html')
        #return 'Hello, World !' + str(infectionProb)

if __name__ == "__main__":
    app.run(debug=True)
