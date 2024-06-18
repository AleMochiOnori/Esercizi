class Film:
    def __init__(self,id,title):
        self.id = id 
        self.title = title



    def set_id(self,id):
        self.id = id

    def set_title(self,title):
        self.title = title

    

    def get_Id(self):
        return self.id
    
    def get_title(self):
        return self.title
    

    def isEqual(self,otherFilm):
        if self.id == otherFilm:
            return True




            
