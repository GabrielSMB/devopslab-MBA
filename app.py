from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Build and Run done"

if __name__ == '__main__':
    app.run()