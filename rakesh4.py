from flask import Flask
app=Flask(__name__)

@app.route("/")
def rakesh4():
    return "Welcome to Flask Application"
    
if __name__=='__main__':
    app.run(debug=True)
    