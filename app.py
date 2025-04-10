from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return " Hello Liaplus team  from Flask deployed on Azure App Service!"

if __name__ == '__main__':
    app.run()

