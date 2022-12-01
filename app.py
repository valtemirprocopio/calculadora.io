from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods= ['POST','GET'])
def index():
    soma = ''
    if request.method == 'POST' and 'a' in request.form and 'b' in request.form:
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        soma = a + b
    return render_template("index.html",soma = soma)
    
if __name__ == '__main__':
    app.run(debug = True)