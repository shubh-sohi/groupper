import math as math
import matplotlib.pyplot as m


def open_file(file, ok):
    Xvalues = []
    Yvalues = []
    f = open(file, ok)
    for line in f:
        splitline = line.rstrip().split(",")
        Xvalues.append(splitline[0])
        Yvalues.append(splitline[1])
        Xvalues = [int(i) for i in Xvalues]
        Yvalues = [int(i) for i in Yvalues]
    return (Xvalues, Yvalues)

values = open_file("locationA.txt", "r")
Xvalues = values[0]
Yvalues = values[1]
maxX = max(Xvalues)
maxY = max(Yvalues)

def make_groups():
    Xgroups = []
    Ygroups = []
    for i in range(number_groups):
        val_inGroup = round(len(Xvalues)/number_groups)

        if i == number_groups-1:
            # print("yes")
            Xgroups.append(Xvalues[val_inGroup * i:len(Xvalues)])
            Ygroups.append(Yvalues[val_inGroup * i:len(Yvalues)])
        else:
            Xgroups.append(Xvalues[val_inGroup*i:val_inGroup*(i+1)])
            Ygroups.append(Yvalues[val_inGroup*i:val_inGroup*(i+1)])
    return (Xgroups, Ygroups)

def compute_average(groups):
    Xaverages = []
    Yaverages = []
    for i in range(number_groups):
        if len(groups[0][i]) == 0:
            Xaverages.append(0)
            Yaverages.append(0)
        else:
            Xaverages.append(sum(groups[0][i])/len(groups[0][i]))
            Yaverages.append(sum(groups[1][i]) / len(groups[1][i]))
    return (Xaverages, Yaverages)

def distance_calculator(pointX, pointY, averageX, averageY):
    distance = math.sqrt(math.pow((averageX - pointX),2)+ math.pow((averageY-pointY), 2))
    return distance



def good_stuff(given_groups):

    averages = compute_average(given_groups)
    groups = 0
    while groups < (number_groups):
        val_in_groups = 0
        while val_in_groups < len(given_groups[0][groups]):
            pt1 = given_groups[0][groups][val_in_groups]
            pt2 = given_groups[1][groups][val_in_groups]
            own_dist = distance_calculator(pt1,pt2,averages[0][groups], averages[1][groups])
            index_averages = 0
            inrCtr = 0
            is_other_small = []
            while index_averages < len(averages[0]):
                if groups != index_averages:
                    other_dist = (distance_calculator(pt1, pt2,averages[0][index_averages], averages[1][index_averages]))
                    is_other_small.append([other_dist, index_averages])
                index_averages+=1
            min_other = (min(is_other_small))
            if min_other[0] < own_dist:
                given_groups[0][groups].pop(val_in_groups)
                given_groups[1][groups].pop(val_in_groups)
                given_groups[0][min_other[1]].append(pt1)
                given_groups[1][min_other[1]].append(pt2)
                good_stuff(given_groups)
            val_in_groups +=1

        groups +=1

def plot():
    counter = 0
    for i in range(number_groups):
        for j in range(len(groups[0][i])):
            # print(groups[0][i][j],",", groups[1][i][j])
            if counter == 0 :
                m.plot(groups[0][i][j], groups[1][i][j], 'og')
            if counter == 1 :
                m.plot(groups[0][i][j], groups[1][i][j], 'or')
            if counter == 2:
                m.plot(groups[0][i][j], groups[1][i][j], 'ob')
            if counter == 3 :
                m.plot(groups[0][i][j], groups[1][i][j], 'oy')
            if counter == 4:
                m.plot(groups[0][i][j], groups[1][i][j], 'ok')
            # if counter == 5:
            #     m.plot(groups[0][i][j], groups[1][i][j], 'pink')
        counter+=1
    for x in range(len(averages[0])):
        m.plot(averages[0][x], averages[1][x], 'oc', marker = 'x')
    # print(maxX, maxY)
    m.xlim(0, maxX+10)
    m.ylim(0, maxY+10)
    m.xlabel("vitamin c")
    m.ylabel("GLA VALUES")
    m.title("groupper")
    m.show()

# plot()
check_for_the_best = []
for i in range(2,5):
    inner = []
    innerSum = 0
    number_groups = i
    groups = make_groups()
    # print(groups[0], '\n', groups[1])
    good_stuff(groups)
    for j in range(len(groups[0])):
        if len(groups[0][j]) != 0:
            inner.append((max(groups[0][j])-min(groups[0][j]))+(max(groups[1][j])-min(groups[1][j])))
    # print(groups[0], '\n', groups[1],'\n')
    averages = compute_average(groups)
    plot()
    check_for_the_best.append(sum(inner))


# for i in check_for_the_best:
#     if i[1] ==
for i in range(len(check_for_the_best)):
    if check_for_the_best[i] == min(check_for_the_best):
        print("the best grouping is with",i+2,"groups")