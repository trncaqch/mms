import pandas

df = pandas.read_csv('csv/photos_tags.csv', names = ["id", "tag"])
#print df


tagsDf = pandas.read_csv('csv/tags.csv', names = ["tags", "n"])


print tagsDf.get_value(1,'tags')


tagList = []

for i in tagsDf.tags:
    tagList.append(i)
print tagList

tagList[0]

matrix = pandas.DataFrame(data = None, index = tagList, columns = tagList)






#print df.loc[0,"tag"]