from flask import Flask, render_template,request
import backend

app=Flask(__name__)#helps flask know where the flask files are

@app.route("/", methods = ["GET", "POST"])#/ means when page is accessed execute home. page can handle get or post requests
def home():
    if request.method == "GET": # Display input form when page is accessed.
        return render_template("index.html")#looks for this file in directory
    if request.method == "POST": #when convert button is pressed
        text=request.form.get("textbox") #assign input from user to variable text
        return render_template ("index.html", 
        output=backend.meters_feet(float(text)),#converts user input from HTML form from a string to a float
        user_text=text)

# Check if the script is the main program being run and not imported
if __name__ == "__main__":
    app.run()