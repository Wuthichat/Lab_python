import math
#print(math.pi)

while True:

    def Rectangular_func(High,Length,Width):
        result = High*Length*Width
        return result

    def Sphere_func(Radius):
        result = 4/3*(math.pi)*(Radius**3)
        return result

    def Cone_func(Radius,High):
        result = 1/3*(math.pi)*(Radius**2)*High
        return result

    def Manu_func(Manu):
        if Manu == 1:
            H = int(input("High: "))
            L = int(input("Length: "))
            W = int(input("Width: "))
            Volume_rectangular = Rectangular_func(H,L,W)
            print("Volume = ",Volume_rectangular)
            
        elif Manu == 2:
            R = int(input("Radius: "))
            Volume_sphere = Sphere_func(R)
            print("Volume = ",Volume_sphere)
            
        elif Manu == 3:
            R = int(input("Radius: "))
            H = int(input("High: "))
            Volume_cone = Cone_func(R,H)
            print("Volume = ",Volume_cone)
            
        else:
            print("... No function \n")
        
    print(
"""Mode1: rectangular prism
Mode2: sphere
Mode3: cone
-------------------------------""")
    
    Choice = int(input("Select Mode: "))
    Manu_func(Choice)

