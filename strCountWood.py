#Program to count the occurrence of ‘wood’ in the string
#“How much wood would a woodchuck chuck if a woodchuck could chuck wood?”
str = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
length = len(str)
pos = 0
count = 0
if(str.find('wood',pos,) != -1):
    pos = str.find('wood')
    count=count+1
    continue
print(count)
