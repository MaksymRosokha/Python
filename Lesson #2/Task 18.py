import random

def printKubeInfo(kube):
    for i in range(1, 7):
        print(f"{i} was {kube[i]} times")

kubeInfo = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(1000):
    randNumber = random.randint(1, 6)
    if randNumber == 1:
        kubeInfo[1] += 1
    elif randNumber == 2:
        kubeInfo[2] += 1
    elif randNumber == 3:
        kubeInfo[3] += 1
    elif randNumber == 4:
        kubeInfo[4] += 1
    elif randNumber == 5:
        kubeInfo[5] += 1
    elif randNumber == 6:
        kubeInfo[6] += 1

printKubeInfo(kubeInfo)