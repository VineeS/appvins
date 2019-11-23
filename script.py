from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about") #/ means home page  # the url to access the application
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


    


