# Multilevel Inheritence

class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    basketball = 23
    def isdance(self):
        return f"Yes I dance {self.dance} no of times."

class Grandson(Son):
    dance = 2
    
    def isdance(self):
        return f"Jackson yeah!"\
        f"Yes I dance incridibly {self.dance} no of times."

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())

print(harry.basketball)   #Grandson looks into father for anything if not found in father it goes to grandfather