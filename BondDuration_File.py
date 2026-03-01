import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):

    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    k = np.arange(1, n + 1)
    t = k / ppy

    cf = np.full(n, c)
    cf[-1] = cf[-1] + face

    pv = 1 / ((1 + r) ** k)
    pvcf = cf * pv

    price = np.sum(pvcf)
    duration = np.sum(t * pvcf) / price

    return duration