class ProviderCoverage:
    id: int
    name: str
    has_2G: False
    has_3G: False
    has_4G: False
    zip_code: int

    def __init__(self, id, zip_code):
        self.id = id
        self.zip_code = zip_code

    def setHas2G(self,binary):
        if binary == 1:
            self.has_2G = True
        else :
            self.has_2G =  False

    def setHas3G(self,binary):
        if binary == 1:
            self.has_3G = True
        else:
            self.has_3G = False

    def setHas4G(self,binary):
        if binary == 1:
            self.has_4G = True
        else :
            self.has_4G = False

    def setName(self,name):
        self.name = name



