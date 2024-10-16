from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input_form():
    return render_template('input_form.html')

@app.route('/result', methods=['POST'])
def result_page():
    # Get the data from the form
    data = request.form.get('data')  # Using .get() for safe access
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
