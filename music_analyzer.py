
# this function reads in and parses the data from the playlist
def readFile(filepath):
    file = open(filepath, "r", encoding="utf-16")
    lines = file.read()
    parse = []
    List = lines.split("\n")
    for i in List:
        parse.append(i.split("\t"))

    return parse

# this function gets all of the years in the playlist


def getYearList(lines):
    yearList = []
    k = 0
    for i in lines:
        if k < getSize(lines):
            yearList.append(lines[k][16])
            k += 1
        else:
            break

    return yearList

# this funciton will get the size of the playlist


def getSize(lines):
    counter = 0
    for i in lines:
        counter += 1

    return counter - 1

# this function gets the amount of songs that were released in every year


def songsPerYear(yearList):
    years = []
    i = 0
    n = 0
    years.append(yearList[1])
    for x in yearList:
        if yearList[i] not in years:
            years.append(yearList[i])
        i += 1
    years.remove("Year")
    years.remove("")
    for y in years:
        count = yearList.count(years[n])
        print(count, " songs from ", years[n], "\n")
        n += 1

# this gets the longest song in the playlist by artist and name


def getLongestSong(lines):
    # 7
    marker = 0
    i = 0
    intList = []
    numbers = []
    k = 0
    while k < getSize(lines):
        intList.append(lines[k][11])
        k += 1
    intList.remove(intList[0])
    for j in intList:
        numbers.append(int(intList[i]))
        i += 1
    numbers.sort()
    result = numbers[len(numbers)-2]
    mark = str(numbers[len(numbers)-2])
    n = 0
    for r in lines:
        if lines[n][11] == mark:
            key = n
            break
        n += 1
    name = lines[key][0]
    artist = lines[key][1]
    print("the longest song is", name, "by", artist, "(", result, ")\n")

# this gets the shortest song in playlist by artist and name


def getShortestSong(lines):
    # 7
    marker = 0
    i = 0
    intList = []
    numbers = []
    k = 0
    while k < getSize(lines):
        intList.append(lines[k][11])
        k += 1
    intList.remove(intList[0])
    for j in intList:
        numbers.append(int(intList[i]))
        i += 1
    numbers.sort()
    numbers.reverse()
    result = numbers[len(numbers)-2]
    mark = str(numbers[len(numbers)-2])
    n = 0
    for r in lines:
        if lines[n][11] == mark:
            key = n
            break
        n += 1
    name = lines[key][0]
    artist = lines[key][1]
    print("the shortest song is", name, "by", artist, "(", result, ")\n")

# this function gets the songs that have been played as well as not played


def songsPlayed(lines):

    counter = 0
    for x in range(getSize(lines)-2):
        if lines[x][25] == '':
            counter += 1

    played = getSize(lines) - counter

    print(played, "songs have been played\n")
    print(counter, "songs have not been played\n")

# this function gets the genres from the playlist


def getGenre(lines):
    g = []
    for x in range(getSize(lines)-2):
        g.append(lines[x][9])
    g = list(set(g))
    return g

# this function counts the amount of songs per genre


def getGenreData(lines, names):
    amount = []
    counter = 0
    for name in names:
        amount.append(counter)
        counter = 0
        for x in range(getSize(lines)-2):
            if lines[x][9] == name:
                counter += 1
    k = 0
    names.remove('Genre')
    amount.remove(0)
    names.remove('Soundtrack')
    for name in names:
        print(amount[k], "songs from", name,"\n")
        k += 1

# this funciton gets the shortest and longest songs for each genre by time, name, and artist


def songInGenre(lines, names):
    mark = 1
    for name in names:
        short = int((lines[1][11]))
        print("shortest song in ", name, ":")
        for x in range(getSize(lines)-2):
            if name == lines[x][9] and int((lines[x][11])) <= short:
                short = int((lines[x][11]))
                mark = x
        print(short, "in length", ",it is by",
              lines[mark][1], "its called", lines[mark][0], "\n")
    mark = 1
    for name in names:
        big = int((lines[1][11]))
        print("longest song in ", name, ":")
        for x in range(getSize(lines)-2):
            if name == lines[x][9] and int((lines[x][11])) >= big:
                big = int((lines[x][11]))
                mark = x
        print(big, "in length", ",it is by",
              lines[mark][1], "its called", lines[mark][0], "\n")

# main function


def main():
    
    filepath = input("Enter a playlist file to analyze:\n")
    lines = readFile(filepath)
    yearList = getYearList(lines)
    print("total number of songs is: ", getSize(lines), "\n")
    songsPerYear(yearList)
    getLongestSong(lines)
    getShortestSong(lines)
    songsPlayed(lines)
    g = getGenre(lines)
    getGenreData(lines, g)
    songInGenre(lines, g)


main()
#plays = 25
#Genra = 9
