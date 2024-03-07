class Player:
    name = input("Enter your name:")
    def __init__(self,name):
        self.name = name
    
    def  get_name(self):
        return self._name
    
    def set_name(self,name):
        if len(name) <= 25:
            self._name = name
        else:
            print('Nom incorrect(25 caractères max.)')
    
    def one_method():
        pass

    def onather_method():
        pass

    name = property(get_name,set_name)
    one_method = staticmethod(one_method)
    onather_method = classmethod(onather_method)