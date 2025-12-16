z = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
aa = {}
for ab in z:
    ac = ab[0]
    if ac in aa:
        aa[ac].append(ab)
    else:
        aa[ac] = [ab]
print(aa)
