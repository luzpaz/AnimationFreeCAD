from PyFlow.Packages.Dalmau.Class.Rotation import Rotation
from PyFlow.Packages.Dalmau.Class.Animation import Animation
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Mouvement import *
from FreeCAD import Vector
from Qt.QtWidgets import *

import FreeCAD

class RotationNode(NodeAnimation):
    def __init__(self, name):
        super(RotationNode, self).__init__(name)
        self.createInputPin("Axe de rotation", "VectorPin", Vector(0,0,1))
        self.createInputPin("Centre de rotation", "VectorPin")
        self.createInputPin("Angle au debut de la rotation", "FloatPin")
        self.createInputPin("Angle a la fin de la rotation", "FloatPin")
        self.createOutputPin("Angle final", "FloatPin")
        self.duree = self.createInputPin("Duree", "FloatPin")

    def compute(self, *args, **kwargs):  
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")  
        if(self.getData("Duree") <= 0):
            return FenetreErreur("Erreur", self.name, self.duree.name, "La durée ne peut pas être inférieure ou égale à 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        axeDeRotation = self.getData("Axe de rotation")        
        centreDeRotation = self.getData("Centre de rotation")        
        angleDeDebut = self.getData("Angle au debut de la rotation")        
        angleDeFin = self.getData("Angle a la fin de la rotation")  

        duree = self.getData("Duree")        
        estBoucle = self.getData("Boucle")        
        estAllerRetour = self.getData("Aller-retour")        

        rotation = Rotation(axeDeRotation, centreDeRotation, angleDeDebut, angleDeFin,self)
        animation = Animation(estBoucle, estAllerRetour, self)
        animation.executionDuree(rotation,objet,duree)

        self.setData("Position finale", objet.Placement.Base)
        self.setData("Angle final", angleDeFin)
        self.setData("Objet use", objet.Label)

    @staticmethod
    def category():
        return 'Rotation|Durée'

    @staticmethod
    def description():
        return "Fait tourner des objets."