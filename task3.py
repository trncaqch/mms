import pandas
import numpy
import math


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

#this will be our output, it does have a form of a matrix order len(tags)*5
popTagsIDF = pandas.DataFrame(columns = tags, index=range(5))

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
            valueIDF = float(float(matrix[selectedTag][currentTag]) * float(math.log(10000/float(tagsNo['n'][currentTag]))))
            
            if valueIDF<maxOccurrence:
                continue

            maxCurrentTag = currentTag
            maxOccurrence = valueIDF

        tagList1.remove(maxCurrentTag)
        popTagsIDF[selectedTag][n] = (maxCurrentTag, float(maxOccurrence))
        n += 1

    tagList.insert(selectedTagIndex, selectedTag) #put back the selected tag in the list for next selected tags
    tagList1 = tagList[:]

print popTagsIDF
