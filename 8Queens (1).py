import random

def initializePopulation():
    Return = []
    for i in range (0,4):
        temp = []
        while len(temp)!=8:
            Int = random.randrange(0,8)
            if Int in temp:
                continue
            else:
                temp.append(Int)
        Return.append(temp)
    return Return

def MatrixZero(values):
    Max=[]
    for i in range(0,8):
        temp = []
        for j in range(0, 8):
            temp.append(0)
        Max.append(temp)
    for r in range(0,8):
        Max[r][int(values[r])]=1
    return Max


def D0(r,c,matric):
    Max = matric
    acceptance = True
    for y in range(0, 8):
        if Max[y][c] == 1:
            if y != r:
                acceptance = False
    return acceptance

def D1(r,c,y,matric):
    Max=matric
    acceptance = True
    while r <= 7 and c <= 7:
        if Max[r][c] == 1 and c != y:
            acceptance =  False
            break
        c += 1
        r += 1
    return acceptance

def D2(r,c,y,matric):
    Max=matric
    acceptance = True
    while r >= 0 and c >= 0:
        if Max[r][c] == 1 and c != y:
            acceptance = False
            break
        c -= 1
        r -= 1
    return acceptance

def D3(r,c,y,matric):
    Max=matric
    acceptance = True
    while r >= 0 and c <=7:
        if Max[r][c] == 1 and c != y:
            acceptance =  False
            break
        c += 1
        r -= 1
    return acceptance

def D4(r,c,y,matric):
    Max=matric
    acceptance= True
    while r <= 7 and c >= 0:
        if Max[r][c] == 1 and c != y:
            acceptance = False
            break
        c -= 1
        r += 1
    return acceptance

def fitness(value):
    mat=MatrixZero(value)
    Count = 0
    for i in range(0, 8):
        acceptance = True
        x = mat[i].index(1)
        acceptance = D1(i,x,x,mat) and D2(i,x,x,mat) and D3(i,x,x,mat) and D4(i,x,x,mat) and D0(i,x,mat)
        if acceptance == True:
                Count+=1

    return Count

def Crossover(Values1,Values2):
    NewValues = []
    NewValues1 = []
    for x in range(0,4):
        NewValues.append(Values1[x])
        NewValues1.append(Values2[x])
    for x in range(4,8):
        NewValues.append(Values2[x])
        NewValues1.append(Values1[x])
    return NewValues,NewValues1

def Mutation(Value):
    NewValue = []
    index= random.randrange(0,8)
    NewIndex = random.randrange(0,8)

    for x in range(0,8):
        if x==index:
            NewValue.append(NewIndex)
        else:
            NewValue.append(Value[x])

    return NewValue

def parentSelection(one,two,three,four):
    options = [[fitness(one),one],[fitness(two),two],[fitness(three),three],[fitness(four),four]]
    options.sort()
    return options




ValueOfFitness=0
counter=0
population = initializePopulation()
while counter<=500:
    temp = parentSelection(population[0],population[1],population[2],population[3])
    parent1 = temp[2][1]
    parent2 = temp[3][1]

    temp = Crossover(parent1,parent2)
    child1 = temp[0]
    child2 = temp[1]

    child1 = Mutation(child1)
    child2 = Mutation(child2)

    ValueOfFitness = max(fitness(child1),fitness(child2),fitness(parent1),fitness(parent2))
    if ValueOfFitness == 8:
        print("number of Iterations are ",counter)
        if fitness(child1) == 8:
            print(child1)
        elif fitness(child2) == 8:
            print(child2)
        elif fitness(parent1) == 8:
            print(parent1)
        else:
            print(parent2)
        break
    population[0]=parent1
    population[1]=parent2
    population[2]=child2
    population[3]=child1

    counter+=1
if counter >=500:
    print("Re-run the program")
