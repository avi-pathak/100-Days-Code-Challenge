def lagDuration(h1, m1, h2, m2, k):
    intime = h1 + k
    delaysec = m1-m2
    delayhour=intime - h2
    delayhour *= 60
    return (delayhour+delaysec)
