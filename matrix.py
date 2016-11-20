import pandas
import numpy

df = pandas.DataFrame
#print df.empty

photo_tags = pandas.read_csv('csv/photos_tags.csv', names = ["id", "tag"])
#print photo_tags


#ordered list of tags
tagsDf = pandas.read_csv('csv/tags.csv', names = ["tags", "n"])

tagList = []

for i in tagsDf.tags:
    tagList.append(i)

#creation of co-occurence matrix
matrix = pandas.DataFrame(data = None, index = tagList, columns = tagList)

#initialize values (NaN for the symmetrical axis)
for i in tagList:
    matrix[i]=0
    matrix[i][i] = numpy.nan




#count co_occurence
idCount = 1

while idCount<=24999:
    if photo_tags[photo_tags['id']==idCount].empty:
        pass
    else:
        common_tags = photo_tags[photo_tags['id']==idCount].tag
        for tag1 in common_tags:
            common_tags2 = list(set(common_tags) - set(tag1))
            for tag2 in common_tags2:
                matrix[tag1][tag2]+=1
              
    idCount+=1


for i in photo_tags[photo_tags['id']==5].tag:
    print i

print matrix


matrix.to_csv('matrix.csv' , sep = ',' )








