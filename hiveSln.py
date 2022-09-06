import numpy as np
import itertools
import random as rand


def validate(rr, kr):
    gap = np.array([])
    for s in range(0, 6):
        tGap = 38-kr[s]-kr[0 if s+1 == 6 else s+1]
        if np.any(rr == tGap):
            rr = rr[rr != tGap]
            gap = np.append(gap, tGap)
        else:
            return False
    fcR = fiveCheck(38-kr[0]-kr[3], 38-kr[1]-kr[4], 38-kr[2]-kr[5], rr)
    if fcR == False or fcR[0] == False:
        return False
    if fourCheck(38-gap[0]-gap[2], 38-gap[1]-gap[3], 38-gap[2]-gap[4], 38-gap[3]-gap[5], 38-gap[4]-gap[0], 38-gap[5]-gap[1], fcR[1][1::]) == False:
        return False
    return True


def fourCheck(g0, g1, g2, g3, g4, g5, rr):
    key = rr[0:2]
    key1 = rr[2:4]
    key2 = rr[4:6]
    for k in key:
        for k1 in key1:
            for k2 in key2:
                if k+k1 == g5 and k1+k2 == g0:
                    ok = tuple(filter(lambda item: item != k, key))[0]
                    ok1 = tuple(filter(lambda item: item != k1, key1))[0]
                    ok2 = tuple(filter(lambda item: item != k2, key2))[0]
                    if ok + k2 == g1 and ok1+ok == g2 and ok1+ok2 == g3 and ok2+k == g4:
                        return True
    return False


def tfl(tuple, rr):
    for t in tuple:
        rr = rr[rr != t]
    return rr


def fiveCheck(ttl, ttl2, ttl3, rr):
    idx = 3
    for keys in itertools.permutations(rr, idx):
        if sum(keys) == ttl:
            for i in keys:
                tfl2 = tfl(keys, rr)
                for keys2 in itertools.permutations(tfl2, idx-1):
                    if sum(keys2, i) == ttl2:
                        tfl3 = tfl(keys2, tfl2)
                        for keys3 in itertools.permutations(tfl3, idx-1):
                            if sum(keys3, i) == ttl3:
                                return True, reOrder(list(keys), i)+list(keys2)+list(keys3)
    return False


def reOrder(g, mx):
    while g[0] != mx:
        g.append(g.pop(0))
    return g


def maxFirst(g):
    mx = max(g)
    while g[0] != mx:
        g.append(g.pop(0))
    return g


res = np.array('')
cnt = 0
with open('result.txt', 'w') as f:
    for keys in itertools.permutations(range(1, 20), 6):
        rr = np.array(range(1, 20))
        kr = np.array(keys)
        for k in kr:
            rr = rr[rr != k]
        if validate(rr, kr) == True:
            tmp = ','.join(str(x) for x in maxFirst(list(keys)))
            if np.any(res == tmp) == False:
                res = np.append(res, tmp)
                f.writelines(tmp + '\n')
                print("Got an answer!" + res)
