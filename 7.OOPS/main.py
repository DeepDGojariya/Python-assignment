class Country:
    avg_population = 40000
    def __init__(self, name, code):
        if(len(str(code)) != 3):
            raise(ValueError("Country Code should be 3 chars long"))
        if(isinstance(name, str) and isinstance(code, str)):
            self.country_name = name
            self.country_code = code
        else:
            raise(ValueError("input should be string."))
    

    def country_short_form(name):
        if(not isinstance(name,str)):
            raise(ValueError("Input should be a string."))
        return name[:2].upper()
    
    def is_densly_populated(self,population):
        if(not isinstance(population,int)):
            raise(ValueError("Input should be an integer."))
        return population>self.avg_population
            

