import matplotlib.pyplot as plt
import csv



def main():
    makePlot(getData())

def getData():
    with open('BTC.csv', 'r') as f:
        data = list(csv.reader(f, delimiter=','))
    return data

#change to dictionary for each day of the year

def makePlot(arr):
    plt.ylabel('ROC')
    plt.xlabel('Time')
    aa= True
    i = 2014
    j = "12"
    years = []
    all = []
    while(aa):
        yAxis = makeYaxis(arr, str(i) + "-" + j)
        xAxis = makeXaxis(arr, str(i) + "-" + j)
        plt.plot(xAxis, yAxis)
        all.append(xAxis)
        years.append(str(i))
        i += 1
        if (i == 2019):
            aa = False
    plt.legend(years)
    plt.show()
    #plt.savefig("one.pdf")


def makeXaxis(arr, year):
    xAxis = []
    aa = True
    i = 1
    while aa:
        if year in arr[i][0]:
            a = arr[i][0]
            b = a[5:7]
            c = a[8:len(a)]
            day = int(b)*30-30+int(c)
            xAxis.append(day)
        i += 1
        if i == len(arr)-1:
            aa = False
    return xAxis

def makeYaxis(arr, year):
    yAxis = []
    aa = True
    i = 2
    while aa:
        if year in arr[i][0]:
            closePrice = float(arr[i][5])
            prePrice = float(arr[i-1][5])
            rot = (((closePrice-prePrice)/prePrice)*100)
            yAxis.append(rot)
        i+=1
        if i == len(arr):
            aa = False
    return yAxis


if __name__== "__main__":
  main()