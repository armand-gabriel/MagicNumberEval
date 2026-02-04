from common.iview import IView
from common.imodel import IModel
from common.icontroller import IController


class View(IView):
    def setActionPerformer(self, actionPerformer: IController) -> None:
        self.actionPerformer = actionPerformer

    def setModel(self, model: IModel) -> None:
        self.model = model

    def setController(self, controller: IController) -> None:
        self.controller = controller

    def showMessage(self, message: str) -> None:
        print(message)

    def askProposal(self) -> int:
        proposal_count = self.model.getProposalCount()
        max_number_proposal = self.model.getMaxNumberOfProposals()
        remaining_count = max_number_proposal - proposal_count
        print("Il vous reste " + str(remaining_count) + " tentatives.")
        proposition = int(input("Entrez une proposition de nombre : "))
        return proposition
