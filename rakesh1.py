from flask import Flask
app=Flask(__name__)

@app.route("/")
def rakesh1():
    return "Hello Rakesh welcome"
    
if __name__=='__main__':
    app.run(debug=True)
    