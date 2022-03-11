from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *

class getVectorValue(NodeBase):
    def __init__(self, name):
        super(getVectorValue, self).__init__(name)
        self.createInputPin("Vecteur", "VectorPin")
        self.createOutputPin("x", "FloatPin")
        self.createOutputPin("y", "FloatPin")
        self.createOutputPin("z", "FloatPin")
        
    def compute(self, *args, **kwargs):
        vecteur = self.getData("Vecteur")
        self.setData("x", vecteur.x)
        self.setData("y", vecteur.y)
        self.setData("z", vecteur.z)

    @staticmethod
    def category():
        return 'Vector'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Eclate un vecteur en retournant ses trois composantes."