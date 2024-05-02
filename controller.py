from model import HelloWorldModel

class HelloWorldController:
    def __init__(self, model):
        self.model = model

    def get_message(self):
        return self.model.message