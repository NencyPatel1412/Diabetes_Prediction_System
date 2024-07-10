from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('Diabetes.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('pages/try.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    arr = np.array([[data1, data2, data3, data4,data5,data6,data7,data8]])
    pred = model.predict(arr)
    return render_template('pages/after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')














