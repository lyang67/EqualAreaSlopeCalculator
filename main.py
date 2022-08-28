
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def read_area_file(fileName):
    import csv

    catchmentPoints = []

    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        yIntercept = 0
        catchmentInitialDistance = 0
        line_count = 0
        for row in csv_reader:
            #individual catchment points
            #elevation, distance, area
            catchmentPointData = [float(row[1]), float(row[0]), float(row[2])]

            #append this to main list of catchment point data
            catchmentPoints.append(catchmentPointData)

        return catchmentPoints

def processCatchmentPointsArea(listOfCatchmentPoints):
        numCatchmentPoints = len(listOfCatchmentPoints)
        print(numCatchmentPoints)

        areaAfterDistance = calculateTotalArea(listOfCatchmentPoints)

        #lots of magic numbers here, do not try this at home
        cumulativeAreaUnderDistance = listOfCatchmentPoints[0][2]
        initialElevation = listOfCatchmentPoints[0][0]
        initialDistanceFromCatchmentOutlet = listOfCatchmentPoints[0][1]

        maxElevation = listOfCatchmentPoints[numCatchmentPoints - 1][0]
        maxDistanceFromOutlet = listOfCatchmentPoints[numCatchmentPoints - 1][1]
        i = 1
        #iterate thru all the distance points, start with the one closest to the catchment but not on the catchment
        #list of catchments starts AT the catchment at index 0
        while (i<numCatchmentPoints):
            currentElevation = listOfCatchmentPoints[i][0]
            currentAreaFromLastPoint = listOfCatchmentPoints[i][2]
            totalDistanceFromCatchmentOutlet = listOfCatchmentPoints[i][1]

            areaAfterDistance -= currentAreaFromLastPoint
            cumulativeAreaUnderDistance += currentAreaFromLastPoint

            slope = (currentElevation - initialElevation)/(totalDistanceFromCatchmentOutlet)
            areaUnderStraightSlope = (slope * totalDistanceFromCatchmentOutlet**2)/2 + initialElevation * totalDistanceFromCatchmentOutlet
            areaEnclosedBetween1 = areaUnderStraightSlope - cumulativeAreaUnderDistance

            areaUnderStraightAfterDistance = ((slope * maxDistanceFromOutlet**2)/2 + initialElevation * maxDistanceFromOutlet) - areaUnderStraightSlope
            areaEnclosedBetween2 = areaAfterDistance - areaUnderStraightAfterDistance

            i +=1
            print(str.format("Slope is {0} at {1} distance from outlet and {2} elevation with cumulative area {3} at point {4}", slope, totalDistanceFromCatchmentOutlet, currentElevation, cumulativeAreaUnderDistance, i))
            print(str.format("Area under first curve is {0}", areaEnclosedBetween1))
            print(str.format("Area under second  curve is {0}", areaEnclosedBetween2))

def calculateTotalArea(listOfCatchmentPoints):
    i = 1
    numCatchmentPoints = len(listOfCatchmentPoints)
    totalArea = 0
    # iterate thru all the distance points, start with the one closest to the catchment but not on the catchment
    # list of catchments starts AT the catchment at index 0
    while (i < numCatchmentPoints):
        totalArea += listOfCatchmentPoints[i][2]
        i += 1

    return totalArea

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    allCatchmentPoints = read_area_file('AreaCalculationsUTF8.csv')
    processCatchmentPointsArea(allCatchmentPoints)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
