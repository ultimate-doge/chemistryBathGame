# [elem, cn]
# [equation]
# [(states, colors)]
def readIt(fileName):
    info = []
    elems = []
    reactants = []
    products = []
    states = []
    colors = []
    f = open(fileName, 'rt')
    for line in f:
        if line == "\n":
            info += [[elems, reactants, products, states, colors]]
            elems = []
            reactants = []
            products = []
            states = []
            colors = []
        elif elems == [] and reactants == [] and products == []\
                and states == [] and colors == []:
            elems = (line.rstrip("\n")).split()
        else:
            line = line.rstrip("\n")
            if "=" in line:
                temp = line.split("=")
                reactants = temp[0].split("+")
                products = temp[1].split("+")
            else:
                temp = line.split(", ")
                for each in temp:
                    temp2 = each.split()
                    states += [temp2[0]]
                    colors += [" ".join(temp2[1:])]
    info += [[elems, reactants, products, states, colors]]
    f.close()
    print info[0]
    print info[1]
