from flask import Flask
app=Flask(__name__)

@app.route("/")
def rakesh2():
    return "Hello Rakesh welcome to emicon"
    
if __name__=='__main__':
    app.run(debug=True)