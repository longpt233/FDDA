
from entity.sensor import Sensor
import config.config as cf
from entity.corr import Corr3D
from entity.corr import Corr2D
import math
from utils.visuallize import *


SQRT3 = math.sqrt(3)

# return num of colum 
def Fc(w,r):
    tmp = (2 *(w-r) )/ (3* r)
    seil_tmp = int(math.ceil(tmp))
    return seil_tmp + 1

# return number of rows of odd number colum
def Fo(h,r):
    tmp = h/(r*SQRT3)
    seil_tmp = int(math.ceil(tmp))
    return seil_tmp

# return number of rows of even number colum
def Fe(h,r):
    numerator = h - (r *SQRT3)/2
    denominator = r *SQRT3
    tmp = numerator /denominator
    seil_tmp = int(math.ceil(tmp))
    return seil_tmp +1 



# y coordnate of each column  where i denotes the ith column
def Fy(w,r,i):

    # print(w," ",r," ",i)

    if i == 0 :
        return r /2 
    else:
        compare_with_w =r/2 +  (Fc(w, r)-1)*r/2
        if compare_with_w < w : 
            return r/2 + i*3*r/2 
        else:
            return w 

    raise Exception("method not match any case !")


# z coordnate
def Fz(h,r,j, isOld):

    if isOld: 
        return h - (r*SQRT3)/2 - j *r *SQRT3
    else: 
        return h - j * r * SQRT3

    raise Exception("method not match any case !")


def getHexagonCenterPoints(w, h, r):
    listHcp =[]

    num_of_col = Fc(w, r) 

    num_of_old_row = Fo(h, r)
    num_of_even_row = Fe(h, r)

    for col_index in range(num_of_col):
        fy = Fy(w, r, col_index)
        
        if col_index%2 ==1 :   # la so chan -> old 
            for row_index in range(num_of_old_row):
                fz = Fz(h, r, row_index, isOld = True)
                listHcp.append(Corr2D(fy, fz))

        else:
            for row_index in range(num_of_even_row):
                fz = Fz(h, r, row_index, isOld = False)
                listHcp.append(Corr2D(fy, fz))
        
    return listHcp

def ShowHCP():
    listHcp = getHexagonCenterPoints(cf.WIDTH, cf.HEIGHT, cf.RADIUS)
    # print(listHcp.__len__())
    x=[]
    y=[]
    for i in listHcp:
        x.append(i.x)
        y.append(i.y)
    Visualze2D(x, y)


def getDistance2D(corr2D_a, corr2D_b):
    tmp1 = corr2D_a.x - corr2D_b.x
    tmp2 = corr2D_a.y - corr2D_b.y
    tmp3 = tmp1*tmp1 + tmp2*tmp2
    return math.sqrt(tmp3)

def initMove(sensor):

    # get corr2D of sensor
    x_sensor = sensor.corr3D.x
    y_sensor = sensor.corr3D.y
    z_sensor = sensor.corr3D.z
    corr2d_sensor = Corr2D(y_sensor, z_sensor)

    # Coor2D list 
    listHcp = getHexagonCenterPoints(cf.WIDTH, cf.HEIGHT, cf.RADIUS)

    hexagonnNum = len(listHcp)
    dmin = 2* cf.LENGTH
    for hcp in listHcp :
        dtmp = getDistance2D(hcp, corr2d_sensor)
        if dtmp< dmin:
            dmin = dtmp
            p_target = hcp

    sensor.MoveTo(Corr3D(x_sensor, p_target.x, p_target.y))

    # call alg2 here 
    
    return sensor



if __name__ == "__main__": 
    
    ShowHCP()
    