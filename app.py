from flask import Flask, render_template

app=Flask(__name__)#helps flask know where the flask files are

@app.route("/")#home executed when the root URL ("/") of the web application is accessed
def home():
    return render_template("index.html")

# Check if the script is the main program being run and not imported
if __name__ == "__main__":
    app.run()