import matplotlib.pyplot as plt
import csv


def main():
    # Main function
    makePlot(getData())


def getData():
    # uses csv library to make a list of the information in the given file
    with open('BTC.csv', 'r') as f:
        data = list(csv.reader(f, delimiter=','))
    return data


# change to dictionary for each day of the year


def makePlot(arr):
    # makes labels for x and y axis
    plt.ylabel('ROC')
    plt.xlabel('Time')
    # aa is a variable used to make a post condition loop
    aa = True
    # i is the year
    i = 2014
    # j is the month of interest, can be changed to give a yearly look on the rate of change
    j = "12"
    years = []
    all = []
    # post condition loop
    while (aa):
        # uses the functions makeYaxis and makeXaxis to make the values of the x and y axis
        yAxis = makeYaxis(arr, str(i) + "-" + j)
        xAxis = makeXaxis(arr, str(i) + "-" + j)
        plt.plot(xAxis, yAxis)
        all.append(xAxis)
        years.append(str(i))
        i += 1
        if (i == 2019):
            aa = False
    # when loop is done, it draws the plot
    plt.legend(years)
    plt.show()
    # plt.savefig("one.pdf")


def makeXaxis(arr, year):
    # produces values for the xAxis
    xAxis = []
    aa = True
    i = 1
    while aa:
        # based on the way yahoo finance produces stock data files
        if year in arr[i][0]:
            a = arr[i][0]
            b = a[5:7]
            c = a[8:len(a)]
            day = int(b) * 30 - 30 + int(c)
            xAxis.append(day)
        i += 1
        if i == len(arr) - 1:
            aa = False
    return xAxis


def makeYaxis(arr, year):
    # produces the values for the y axis
    yAxis = []
    aa = True
    i = 2
    while aa:
        if year in arr[i][0]:
            # rate of change formula, ((Final - Initial)/ Initial)*100%
            closePrice = float(arr[i][5])
            prePrice = float(arr[i - 1][5])
            rot = (((closePrice - prePrice) / prePrice) * 100)
            yAxis.append(rot)
        i += 1
        if i == len(arr):
            aa = False
    return yAxis


if __name__ == "__main__":
    main()
