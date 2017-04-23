def isChild(x, y):
    return x == 2 * y or x == 2 * y + 1


def isParent(x, y):
    return isChild(y, x)


def edgeexists(x, y):
    return isChild(x, y) or isParent(x, y)


# the above function in one statement
def list_powerset(lst):
    return reduce(lambda rslt, x: rslt + [subset + [x] for subset in rslt],
                  lst, [[]])


for trial in range(100):
    nodes = []
    for i in range(trial):
        nodes.append(i)

    indepsets = []

    for st in list_powerset(nodes):
        tracker = False
        for v in st:
            for w in st:
                if edgeexists(v, w):
                    tracker = True
                    continue
        if not tracker:
            indepsets.append(st)
    print "n = %d, numSets = %d" % (trial, len(indepsets))
