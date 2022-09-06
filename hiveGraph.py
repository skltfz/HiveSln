def draw(keys, gaps, inners):
    k = tuple(keys)
    g = tuple(map(int, gaps))
    inners = tuple(inners)
    c = inners[0]
    i = inners[1::]
    print("O      {k5}      {g5}      {k0}      O".format(
        k5=k[5], g5=g[5], k0=k[0]))
    print("    {g4}      {i4}      {i0}      {g0}    ".format(
        g4=g[4], g0=g[0], i4=i[4], i0=i[0]))
    print("{k4}      {i2}      {c}      {i3}      {k1}".format(
        k4=k[4], i2=i[2], i3=i[3], c=c, k1=k[1]))
    print("    {g3}      {i1}      {i5}      {g1}    ".format(
        g3=g[3], g1=g[1], i1=i[1], i5=i[5]))
    print("O      {k3}      {g2}      {k2}      O".format(
        k3=k[3], g2=g[2], k2=k[2]))
