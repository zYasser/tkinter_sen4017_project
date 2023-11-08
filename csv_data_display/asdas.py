import numpy as np
ratings = np.array([[3, 3, 4, 0, 4, 2, 3, 0],
                    [3, 5, 4, 3, 3, 0, 0, 4],
                    [0, 4, 0, 5, 0, 0, 2, 1],
                    [2, 0, 0, 4, 0, 4, 4, 5]])
Ub = (ratings>0).astype(int)
print(Ub)



def jaccard(a,b):
    return (a*b).sum()/((a+b)>0).sum()

users = ["firechicken","mike0702","zephyros","dadvador"]

simmat=np.zeros((4,4))
for i in range(4):
    for j in range(4):
        simmat[i,j] = jaccard(Ub[i],Ub[j])
        if i<j:
            print(users[i]+'-'+users[j], jaccard(Ub[i],Ub[j]))

print(simmat)
print('---------------------------------------')
def cos(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

simmat=np.zeros((4,4))
for i in range(4):
    for j in range(4):
        simmat[i,j] = cos(Ub[i],Ub[j])
        if i<j:
            print(users[i]+'-'+users[j], cos(Ub[i],Ub[j]))
print(simmat) 