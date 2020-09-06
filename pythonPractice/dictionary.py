a={0:[[1,2,3,4],[2,1,3,5]],1:[[4,6,2,3],[9,3,4,5]]}

def sept(a):
    b={}
    for key,value in a.items():
        b[key]=fooo(value)
    return b


def fooo(value):

    f=[]
    count=0

    for i in range(len(value)):

        row=value[i]
        for j in range(len(row)):
            row[j]+=1
        f.append(row)

    return f


print(sept(a))
