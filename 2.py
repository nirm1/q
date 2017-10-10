class Person:

    def __init__(self, first_name,last_name):
     self.fname=first_name
     self.lname=last_name

 #   def __ptr__(self):


Michal=Person('Michal','Ben Ari')

print(Michal.fname)
print(Michal.lname)

list = [u +1 for u in range(10) if u < 3]
print(list)