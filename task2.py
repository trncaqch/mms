import pandas
import numpy


#create ordered tagList
tagsNo = pandas.read_csv('csv/tags.csv', names = ["n"])

tagsNo.to_csv('csv/tags_modified.csv', sep = ',')


#tags.csv is easier to handle if read properly in a DataFrame with the right headers
tagsNo = pandas.DataFrame.from_csv('csv/tags_modified.csv')


tagList = []

for i in tagsNo.index:
    tagList.append(i)


tags = ["water","people","london"]
tagList1 = tagList[:]


popTags = pandas.DataFrame(columns = tags, index=range(5))

matrix = pandas.DataFrame.from_csv('matrix.csv')

for selectedTag in tags:
    selectedTagIndex = tagList.index(selectedTag)
    n = 0
    tagList.remove(selectedTag)
    tagList1 = tagList[:]
    while n<5:
        maxCurrentTag = ""    
        maxOccurrence = 0

        for currentTag in tagList1:

            if matrix[selectedTag][currentTag]<maxOccurrence:
                continue
            maxCurrentTag = currentTag
            maxOccurrence = matrix[selectedTag][currentTag]
        tagList1.remove(maxCurrentTag)
        popTags[selectedTag][n] = (maxCurrentTag, maxOccurrence)
        n += 1
    tagList.insert(selectedTagIndex, selectedTag)
    tagList1 = tagList[:]
print popTags

