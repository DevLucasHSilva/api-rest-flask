from flask.json import JSONEncoder

class ANIMES(object):
    new_id = 1
    def __init__(self, Name, Autor, Description):
        self.Name = Name
        self.Autor = Autor
        self.Description = Description
        self.id = ANIMES.new_id
        ANIMES.new_id += 1
        
class ANIMESEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ANIMES):
            return obj.__dict__
        return super(ANIMESEncoder,self).default(obj)