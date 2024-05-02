from flask import render_template
from controller import HelloWorldController

class HelloWorldView:
    def __init__(self, controller):
        self.controller = controller

    def render(self):
        message = self.controller.get_message()
        return render_template('index.html', message=message)