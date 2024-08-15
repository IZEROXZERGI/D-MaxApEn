import numpy as np
import math
from algorithms.auto_threshold import auto_threshold
def ApEn(data, smpF, sec,m = 2,auto_selection = 1,threshold = 0.1):
    if len(data.shape)>1:
        if data.shape[0]>data.shape[1]:
            data = data.T
        data = data.astype(np.float64)
        C,n = data.shape
        dtLn = math.floor(n/smpF)
    else:
        data = data.astype(np.float64)
        C=1
        n = len(data)
        dtLn = math.floor(n/smpF)
#     ApEn = np.zeros(shape=(m, int(dtLn/sec)))
    ApEn = []
    N = smpF*sec
    for chnNo in range(0,C):
        # index = 0
        for str_ in range(0, dtLn, sec):
            ent = str_+sec
            if len(data.shape)>1:
                tmpD = (data[chnNo,str_*smpF+1:ent*smpF]).tolist()
            else:
                tmpD = (data[str_*smpF+1:ent*smpF]).tolist()
            if auto_selection == 1:
                threshold = auto_threshold(tmpD)

            else:
                threshold = threshold
            # print(threshold)
            r = (threshold*np.std(tmpD)).tolist()
            # print(r)
            sum0 = 0
            sum1 = 0
            # m = 2

            for i in range(0,(N-m)):
                n = 0
                for j in range(0,(N-m)):
                    if (abs(tmpD[i]-tmpD[j]) <= r and abs(tmpD[i+1]-tmpD[j+1])<=r):
                        n = n + 1
                h = n/(N-m+1)
                # print(i,h)
                sum0 = sum0 + math.log(h)
            pro = sum0/(N-m+1)
            

            for x in range(0,(N-m-1)):
                n1 = 0
                for y in range(0,(N-m-1)):
                    if (abs(tmpD[x]-tmpD[y])<=r and abs(tmpD[x+1]-tmpD[y+1])<=r and abs(tmpD[x+2]-tmpD[y+2])<=r):
                        n1 = n1+1
                h1 = n1/(N-m)
                # print(x,h1)
                sum1 = sum1+math.log(h1)
            pro1 = sum1/(N-m)
            apen = pro-pro1

            ApEn.append(apen)
            # index = index+1



    return np.array(ApEn)