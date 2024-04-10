from flask import Flask
from sqlalchemy import SQLAlchemy
 
app = Flask(__name__)

@app.route("/")
def index():
    return "O Marcelo é careca"

if __name__ == "__main__":
    app.run()