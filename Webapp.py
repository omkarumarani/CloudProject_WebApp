from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello_World():
 return "Hello World"

if __name__== "_main_":
    app.run()
 
 


    