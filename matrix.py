import pandas


df = pandas.DataFrame
print df.empty

photo_tags = pandas.read_csv('csv/photos_tags.csv', names = ["id", "tag"])
#print df


idCount = 0

while idCount<=24999:
    if photo_tags[photo_tags['id']==idCount].empty:
        pass
    else:
        break #define a function that completes co occurence matrix using 
              #photo_tags[photo_tags['id']==5].tag
    idCount+=1


for i in photo_tags[photo_tags['id']==5].tag:
    print i

#print (o.empty)

tagsDf = pandas.read_csv('csv/tags.csv', names = ["tags", "n"])


#print tagsDf.get_value(1,'tags')



tagList = []

for i in tagsDf.tags:
    tagList.append(i)
#print tagList

tagList[0]

matrix = pandas.DataFrame(data = None, index = tagList, columns = tagList)

