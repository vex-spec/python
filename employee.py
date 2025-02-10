class employee :
    def __init__(self,name,position,salary):
        self.name = name
        self.salary = salary
        self.position =position

    def info(self):
        print(self.position,"Is earning",self.salary)



employee1 = employee("John","ceo","345500")
print(employee1.name,"position", "salary")
employee1.info()




employee2 = employee("Jane","managing director","35500")
print(employee2.name,"position","salary")
employee2.info()


employee3 = employee("jun","managing director","35500")
print(employee3.name,"position","salary")
employee3.info()


employee4 = employee("cozmo","managing director","35500")
employee5 = employee("Jane","managing director","35500")
employee6 = employee("Jane","managing director","35500")