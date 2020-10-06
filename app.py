from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "2-factor issue, but now it works\n" 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
