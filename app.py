from flask import Flask

app=Flask(__name__)#helps flask know where the flask files are

@app.route("/")#home executed when the root URL ("/") of the web application is accessed
def home():
    return "hello world"

# Check if the script is the main program being run and not imported
if __name__ == "__main__":
    app.run()