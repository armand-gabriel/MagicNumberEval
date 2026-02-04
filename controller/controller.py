from common.imodel import IModel
from common.iview import IView
from common.icontroller import IController

class Controller(IController):

    def setView(self, view: IView) -> None:
        self.view = view

    def setModel(self, model: IModel) -> None:
        self.model = model

    def start(self) -> None:
        while self.model.getProposalCount() < self.model.getMaxNumberOfProposals():
            num = self.view.askProposal()
            self.performProposeNumber(num)
            if num == self.model.magicNumber:
                break
        else:
            self.view.showMessage(f"Vous avez épuisé vos tentatives. Le nombre était {self.model.magicNumber}.")

    def performProposeNumber(self, num: int) -> None:
        pass
