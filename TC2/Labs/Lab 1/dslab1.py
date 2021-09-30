import pandas as pd
dataSet = pd.read_csv("./Data Set.csv")
print(dataSet.dtypes)

def generateList(dataSet, column):
    return dataSet[str(column)].tolist()

def mean():
    sepalLen = generateList(dataSet, "SepalLengthCm")
    sepalWid = generateList(dataSet, "SepalWidthCm")
    petalLen = generateList(dataSet, "PetalLengthCm")
    petalWid = generateList(dataSet, "PetalWidthCm")

    sepalLenMean = 0
    sepalWidMean = 0
    petalLenMean = 0
    petalWidMean = 0

    for i in sepalLen:
        sepalLenMean += i
    sepalLenMean = sepalLenMean / len(sepalLen)

    for i in sepalWid:
        sepalWidMean += i
    sepalWidMean = sepalWidMean / len(sepalWid)

    for i in petalLen:
        petalLenMean += i
    petalLenMean = petalLenMean / len(petalLen)

    for i in petalWid:
        petalWidMean += i
    petalWidMean = petalWidMean / len(petalWid)
    print(f'SepalLen Mean: {sepalLenMean} sepalWid mean: {sepalWidMean}\npetalLen mean: {petalLenMean} petalWid mean: {petalWidMean}')
    return sepalLenMean, sepalWidMean, petalLenMean, petalWidMean

def median():
    sepalLen = sorted(generateList(dataSet, "SepalLengthCm"))
    sepalWid = sorted(generateList(dataSet, "SepalWidthCm"))
    petalLen = sorted(generateList(dataSet, "PetalLengthCm"))
    petalWid = sorted(generateList(dataSet, "PetalWidthCm"))
    
    sepalLenMeadian = 0
    sepalWidMeadian = 0
    petalLenMeadian = 0
    petalWidMeadian = 0

    if len(sepalLen) % 2 == 0:
        sepalLenMeadian = sepalLen[(len(sepalLen) - 1) // 2]
    else:
        sepalLenMeadian = sepalLen[(len(sepalLen) - 1) // 2] + sepalLen[((len(sepalLen) - 1) // 2) + 1] / 2.0

    if len(sepalWid) % 2 == 0:
        sepalWidMeadian = sepalWid[(len(sepalWid) - 1) // 2]
    else:
        sepalWidMeadian = sepalWid[(len(sepalWid) - 1) // 2] + sepalWid[((len(sepalWid) - 1) // 2) + 1] / 2.0

    if len(petalLen) % 2 == 0:
        petalLenMeadian = petalLen[(len(petalLen) - 1) // 2]
    else:
        petalLenMeadian = petalLen[(len(petalLen) - 1) // 2] + petalWid[((len(petalLen) - 1) // 2) + 1] / 2.0

    if len(petalWid) % 2 == 0:
        petalWidMeadian = petalWid[(len(petalWid) - 1) // 2]
    else:
        petalWidMeadian = petalWid[(len(petalWid) - 1) // 2] + petalWid[((len(petalWid) - 1) // 2) + 1] / 2.0
    
    return f'Sepal Length Meadian: {sepalLenMeadian} Sepal Width meadian: {sepalWidMeadian}\nPetal Length meadian: {petalLenMeadian} Petal Width meadian: {petalWidMeadian}'

def abstractMax(_list):
    return max(set(_list), key=_list.count)

def mode():
    sepalLen = generateList(dataSet, "SepalLengthCm")
    sepalWid = generateList(dataSet, "SepalWidthCm")
    petalLen = generateList(dataSet, "PetalLengthCm")
    petalWid = generateList(dataSet, "PetalWidthCm")

    return f'Sepal Length Mode: {abstractMax(sepalLen)} Sepal Width Mode: {abstractMax(sepalWid)}\nPetal Length: {abstractMax(petalLen)} Petal Width: {abstractMax(petalWid)}'

def variance():
    sepalLen = generateList(dataSet, "SepalLengthCm")
    sepalWid = generateList(dataSet, "SepalWidthCm")
    petalLen = generateList(dataSet, "PetalLengthCm")
    petalWid = generateList(dataSet, "PetalWidthCm")

    var_mean = mean()
    sepalLenVar = 0
    sepalWidVar = 0
    petalLenVar = 0
    petalWidVar = 0


    SLmean = var_mean[0]
    sepalLenVar = sum((i - SLmean) ** 2 for i in sepalLen) / len(sepalLen)

    SWmean = var_mean[1]
    sepalWidVar = sum((i - SWmean) ** 2 for i in sepalWid) / len(sepalWid)

    PLmean = var_mean[2]
    petalLenVar = sum((i - PLmean) ** 2 for i in petalLen) / len(petalLen)

    PWmean = var_mean[3]
    petalWidVar = sum((i - PWmean) ** 2 for i in petalWid) / len(petalWid)

    print(f'Variance Sepallen: {sepalLenVar}, ,  Variance SepalWid: {sepalWidVar}\nVariance petalLen: {petalLenVar}, Variance petalWid: {petalWidVar}')
    return sepalLenVar, sepalWidVar, petalLenVar, petalWidVar

def standarDev():
    variance_var = variance()
    return f'Standard Deviation Sepallen: {variance_var[0] ** 0.5},  Standard Deviation SepalWid: {variance_var[1] ** 0.5}\nStandard Deviation petalLen: {variance_var[2] ** 0.5}, Standard Deviation petalWid: {variance_var[3] ** 0.5}'

def quartileRange():
    sepalLen = generateList(dataSet, "SepalLengthCm")
    sepalWid = generateList(dataSet, "SepalWidthCm")
    petalLen = generateList(dataSet, "PetalLengthCm")
    petalWid = generateList(dataSet, "PetalWidthCm")

    return f'Qurtile Range SepalLen: {max(sepalLen) - min(sepalLen)} Qurtile Range SepalWid: {max(sepalWid) - min(sepalWid)}\nQurtile Range petalLen: {max(petalLen) - min(petalLen)} Qurtile Range petalWid: {max(petalWid) - min(petalWid)}'

print(mean())
print("\n")
print(median())
print("\n")

print(mode())
print("\n")

print(variance())
print("\n")

print(standarDev())
print("\n")

print(quartileRange())



