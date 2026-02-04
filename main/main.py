
from controller.controller import Controller
from model.model import Model
from view.view import View

controller = Controller()
model = Model()
view = View()
controller.setModel(model)
controller.setView(view)

view.setModel(model)
view.setController(controller)

controller.start()
