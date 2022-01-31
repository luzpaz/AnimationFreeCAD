from PyFlow.Packages.Dalmau.Class.Rotation import Rotation
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
import FreeCAD
from FreeCAD import Vector

class RotationSurSoiMemeNode(NodeAnimation):
    
    def __init__(self, name):
        super(RotationSurSoiMemeNode, self).__init__(name)
        self.createInputPin("Axe de rotation", "VectorPin", Vector(0,0,1))
        self.createInputPin("Angle au debut de la rotation", "FloatPin")
        self.createInputPin("Angle a la fin de la rotation", "FloatPin")
        self.createOutputPin("Angle final", "FloatPin")

    def compute(self, *args, **kwargs):
        monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        monAxeDeRotation = self.getData("Axe de rotation")
        monCentreDeRotation = FreeCAD.Vector(0,0,0)
        monAngleDebut = self.getData("Angle au debut de la rotation")
        monAngleFin = self.getData("Angle a la fin de la rotation")
        maDuree = self.getData("Duree deplacement")
        monEstBoucle = self.getData("Boucle")
        monEstAllerRetour = self.getData("Aller-retour")
        
        rotation = Rotation(self, monObjet, monAxeDeRotation, monCentreDeRotation, monAngleDebut, monAngleFin, maDuree, monEstBoucle, monEstAllerRetour)
        rotation.rotation()

        self.setData("Position finale", monObjet.Placement.Base)
        self.setData("Angle final", monAngleFin)

    @staticmethod
    def category():
        return 'Rotation'

    @staticmethod
    def description():
        return "Fait tourner des bails"