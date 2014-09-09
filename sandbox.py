def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    print parts
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)


test = "lan/olum/ben/seni"
numberOfOccurences = test.count("/")
goBack = 2
relativeGoBack = numberOfOccurences - goBack
print findnth(test, "/", relativeGoBack-1)
currentFolder = test[0:3]
print currentFolder