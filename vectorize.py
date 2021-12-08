import numpy as np


def GetDataFromDic(Dict, array):
    try:
        val = Dict.get(array)
        if(val is not None):
            return val
        else:
            return 0
    except:
        return 0


Dict = {1: 10, 2: 12, 3: 13}
array = [1, 2, 3, 4]
vfunc = np.vectorize(GetDataFromDic)
result = vfunc(Dict, array)
print(result)
