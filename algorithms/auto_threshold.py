import numpy as np
import math
def auto_threshold(data):
    N = len(data)
    eii = []
    # Beta  = [ei for ei in data if 20 > abs(ei) > 2]
    for i in range(1,N):
        ei =(data[i]-data[i-1])
        eii.append(ei) 
        # ei =(Beta[i]-Beta[i-1])
        # eii.append(ei) 
        
    Beta  = [ei for ei in eii if 20 > abs(ei) > 2]
    # print(len(Beta)/len(eii))
    sd1 = np.std(Beta)
    sd2 = np.std(data)
    rmax = (-0.02+0.23*(math.sqrt(sd1/sd2))/((N/1000)**(1/4)))
   

    if math.isnan(rmax) ==True:
        # print(rmax,'error data')
        rmax = 0.25
    elif rmax<0:
        # print(rmax,'error data')
        rmax = 0.25
    else:
        pass
    return rmax