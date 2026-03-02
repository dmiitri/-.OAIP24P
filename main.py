from flask import Flask, render_template
app = Flask (__name__)
@app.route ("/")
def about ():
    a = 34
    b = 24
    c = 54
    return render_template("about.html",
                           a=a,
                           b=b,
                           c=c)
@app.route ("/<float:num1>/<op>/<float:num2>/")
def calculate (num1, op, num2):
    return render_template ("index.html",
                            num1=num1,
                            operation = op,
                            num2=num2)
if __name__ == "__main__":
    app.run(debug=True)