import datetime

class Event(object):
    def __init__(self,data,name,priorytet):
        pass
    def set_znacznik(self,znacznik):
        self.znacznik=znacznik
    def get_znacznik(self):
        return self.znacznik
    def set_czas_wykonania(self,czasWykonania):
        try:
            czasWykonania=str(czasWykonania)
        except ValueError:
            pass
        self.czas_wykonania=czasWykonania
    def get_czas_wykonania(self):
        return self.czas_wykonania
    def set_planowany_czas(self,czasPlanowany):
        self.planowany_czas = czasPlanowany
    def get_planowany_czas(self):
        return self.planowany_czas
    def set_rzeczywisty_czas(self,czas_rzeczywisty):
        self.czas_rzeczywisty = czas_rzeczywisty
    def get_rzeczywisty_czas(self):
        return self.czas_rzeczywisty
    def set_plany(self,plany):
        self.plany = plany
    def get_plany(self):
        return self.plany
    def set_wnioski(self, wnioski):
        self.wnioski = wnioski
    def get_wnioski(self):
        return self.wnioski

    
