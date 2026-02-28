from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index ():
    r = 12
    pi = 3.14
    otvet = pi * r**2
    return render_template("Flask_Jinja.html",
                           radius = r,
                          otvet = otvet )
if __name__ == '__main__':
    app.run(debug=True)