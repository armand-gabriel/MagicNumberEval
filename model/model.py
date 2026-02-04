import random

from common.imodel import IModel


class Model(IModel):
    # To be completed

    def __init__(self):
        self.magicNumber = random.randint(1, 100)
        self.proposalCount = 0
        self.maxNumberOfProposals = 10

    def compareToMagicNumber(self, num: int) -> int:
        self.proposalCount += 1

        if num < self.magicNumber:
            return -1
        elif num > self.magicNumber:
            return 1
        else:
            return 0

    def getProposalCount(self) -> int:
        return self.proposalCount

    def getMaxNumberOfProposals(self) -> int:
        return self.maxNumberOfProposals