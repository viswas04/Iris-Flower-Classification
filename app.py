from flask import Flask, render_template, request
import model

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def basic():
    if request.method == 'POST':
        sepal_length = float(request.form['sepallength'])
        sepal_width = float(request.form['petalwidth'])
        petal_length = float(request.form['petallength'])
        petal_width = float(request.form['petalwidth'])
        y_pred = [[sepal_length, sepal_width, petal_length, petal_width]]
        trained_model = model.training_model()
        prediction_value = trained_model.predict(y_pred)
        setosa = 'The flower is classified as Setosa'
        versicolor = 'The flower is classified as Versicolor'
        virginica = 'The flower is classified as Virginica'
        if prediction_value == 0:
            return render_template('index.html', setosa=setosa)
        elif prediction_value == 1:
            return render_template('index.html', versicolor=versicolor)
        else:
            return render_template('index.html', virginica=virginica) 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)