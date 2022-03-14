from PyFlow.Packages.Dalmau.Class.TranslationAvecCourbe import TranslationAvecCourbe
from PyFlow.Packages.Dalmau.Class.Mouvement import *
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Animation import Animation

import FreeCAD

class TranslationAvecCourbeNode(NodeAnimation):
    def __init__(self, name):
        super(TranslationAvecCourbeNode, self).__init__(name)
        self.courbe = self.createInputPin("Courbe", "CurvePin", DEFAULT_VALUE_OBJECT_PIN)
        self.duree = self.createInputPin("Duree", "FloatPin")
    
    def compute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")
        if(self.getData("Courbe") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.courbe.name, "Veuillez choisir une courbe à suivre.")  
        if(self.getData("Duree") <= 0):
            return FenetreErreur("Erreur", self.name, self.duree.name, "La durée ne peut pas être inférieure ou égale à 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        courbe = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Courbe"))[0]
        duree = self.getData("Duree")
        estAllerRetour = self.getData("Aller-retour")  
        estBoucle = self.getData("Boucle")
        
        self.mouvement = TranslationAvecCourbe(courbe, self)
        animation = Animation(estBoucle, estAllerRetour, self)
        animation.executionDuree(self.mouvement, objet, duree)

        self.setData("Position finale", objet.Placement.Base)
        self.setData("Objet use", objet.Label)
        
    @staticmethod
    def category():
        return 'Translation|Durée'

    @staticmethod
    def description():
        return "Fait bouger des objets le long d'unr courbe à vitesse uniforme."