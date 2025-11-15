from flask import Flask,render_template
import pickle

# Create flask app
flask_app = Flask(__name__)


# Load the pickle model and processor
with open('model.pkl','rb') as file:
    model=pickle.load(file)
with open('pre.pkl','rb') as file:
    pre=pickle.load(file)

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict",methods=["POST"])
def predict():
    x = [i for i in request.form.values()]
    xpre = pre.transform(x)
    res = model.predict(xpre)
    if res[0]==0:
        res_op ='Non-Diabetic'
    elif res[0]==1:
        res_op = 'Diabetic'
    else:
        res_op='Predict_Diabetic'
    
    res_proba = model.predict_proba(xnew_pre)
    max_prob = np.max(res_proba)
    return render_template("index.html",prediction_text=f"Based on your test results, model has predicted : {res_op} with a {max_prob} probability")

    if __name__=="__main__":
        flask_app.run(debug=True)
