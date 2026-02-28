from flask import Flask, render_template
app = Flask(__name__)
a = 32
b = a * 2
messege = f"Это ваше число = {a}, умноженное на 2 =  {b} "
@app.route('/')
def index():
    return render_template ("Flask_Jinja_2.html",
                            name = "Dima",
                            title = "Home",
                            number = b,
                            messege = messege,
                            Number_2 = a            )
if __name__ == '__main__':
    app.run(debug=True)