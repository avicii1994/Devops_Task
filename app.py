from flask import Flask
from view import HelloWorldView
from controller import HelloWorldController
from model import HelloWorldModel

app = Flask(__name__, template_folder='templates')

model = HelloWorldModel()
controller = HelloWorldController(model)
view = HelloWorldView(controller)

@app.route('/')
def index():
    return view.render()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


