import random
import matplotlib.pyplot as plt

# 랜덤돌리기(공통)
def color (x, y, z, a, b, c) :

    R = random.randrange(x, a)/255
    G = random.randrange(y, b)/255
    B = random.randrange(z, c)/255
    
    return R, G, B


def rancolor() :

    arrayr = []
    rcolor = 0

    while True :
    
        rcolor = color(0, 0, 0, 256, 256, 256)
        x, y, z = rcolor

        if abs(abs(x - y) - abs(x - z)) < 20 :
            arrayr.append(rcolor)

        if len(arrayr) >= 3 :
            break

    return arrayr


def warmcolor() :

    arrayw = []
    wcolor = 0

    while True :
    
        wcolor = color(120, 0, 0, 256, 256, 121)
        x, y, z = wcolor

        if abs(abs(x - y) - abs(x - z)) < 20 :
            arrayw.append(wcolor)

        if len(arrayw) >= 3 :
            break
        


    return arrayw
        


def coolcolor ():

    arrayc = []
    ccolor = 0

    while True :
    
        ccolor = color(0, 0, 120, 121, 256, 256)
        x, y, z = ccolor

        if abs(abs(x - y) - abs(x - z)) < 20 :
            arrayc.append(ccolor)

        if len(arrayc) >= 3 :
            break

    return arrayc

    
def mucolor () :

    arraym = []
    mcolor = 0

    while True :

        a = random.randrange(0, 256)/255
    
        x = a
        y = a
        z = a

        mcolor = (a, a, a)
        
        arraym.append(mcolor)

        if len(arraym) >= 3 :
            break
    
    
    return arraym




print("\n")



while True:
    choose = input ("무엇을 고르시겠습니까? \n 1. 난색\n 2. 한색\n 3. 무채색\n 4. 종료\n\n 선택 : ")
    if choose == '1' :
        print("Your RGB = ", warmcolor() )
        print("\n")
        x_values = [1,2,3]
        y_values = [1,2,3]
        color1 = warmcolor()
        
        plt.scatter(x_values[0],y_values[0],s = 500, c = color1[0])
        plt.scatter(x_values[1],y_values[1],s = 500, c = color1[1])
        plt.scatter(x_values[2],y_values[2],s = 500, c = color1[2])
        plt.show()

    elif choose == '2' :
        print("Your RGB = ", coolcolor() )
        print("\n")
        x_values = [1,2,3]
        y_values = [1,2,3]
        color2 = coolcolor()
        
        plt.scatter(x_values[0],y_values[0],s = 500, c = color2[0])
        plt.scatter(x_values[1],y_values[1],s = 500, c = color2[1])
        plt.scatter(x_values[2],y_values[2],s = 500, c = color2[2])
        plt.show()
    elif choose == '3' : 
        print("Your RGB = ", mucolor() )
        print("\n")
        x_values = [1,2,3]
        y_values = [1,2,3]
        color3 = mucolor()
        
        plt.scatter(x_values[0],y_values[0],s = 500, c = color3[0])
        plt.scatter(x_values[1],y_values[1],s = 500, c = color3[1])
        plt.scatter(x_values[2],y_values[2],s = 500, c = color3[2])
        plt.show()
    elif choose == '4' :
        print("프로그램을 종료합니다.")
        print("\n")
        break
    else :
        print("*값이 올바르지 않아 랜덤으로 추출합니다.* \n Your RGB = ", rancolor())
        print("\n")
        x_values = [1,2,3]
        y_values = [1,2,3]
        color4 = rancolor()
        
        plt.scatter(x_values[0],y_values[0],s = 500, c = color4[0])
        plt.scatter(x_values[1],y_values[1],s = 500, c = color4[1])
        plt.scatter(x_values[2],y_values[2],s = 500, c = color4[2])
        plt.show()
        











