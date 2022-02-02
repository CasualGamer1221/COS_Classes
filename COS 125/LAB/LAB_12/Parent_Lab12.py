import random as rand

class SSBody:
    def __init__ (self):
        self.sats = ()      
        self.mean_distance_from_star = rand.randrange(100,1000000)
        self.radius = rand.randrange(40,10000)
        self.habitability = rand.randint(0,1)
        self.name = rand.choice("test","aquila","smaltor","creeg")
        self.mean_surface_temperature = rand.randrange(-200,700000)
    
    def GET_mean_distance_from_star(self):
        return self.mean_distance_from_star
   
    def GET_radius(self):
        return self.radius
   
    def GET_habitability(self):
        return self.habitability
    
    def GET_name(self):
        return self.name
    
    def GET_mean_surface_temperature(self):
        return self.mean_surface_temperature
    
    def ADD_sats(self):
        asteroids=rand.randrange(0,100)
        moons=rand.randrange(0,100)
        self.sats=(asteroids, moons)
        return self.sats


        
    

    