import re
import sys

note = {}
note_value = {}

favorited = ""
favoriteCount = 0
replyToSN = ""
created = ""
Id = ""
replyToUID = ""
statusSource = ""
screenNam = ""
retweetCount = 0
isRetweet = ""
retweeted = ""


for line in sys.stdin:
    if line != "\n":
        line = line.strip(",")

        value = line.split(",")

        favorited = value [0]
        favoriteCount = value[1]
        replyToSN = value[2]
        created = value[3]
        Id = value[4]
        replyToUID = value[5]
        statusSource = value[6]
        screenNam = value[7]
        retweetCount= value[8]
        isRetweet = value[9]
        retweeted = value[10]

        try:
            favoriteCount = int(favoriteCount)
            retweetCount = int(retweetCount)
        except ValueError:
            continue
            

        note[Id] = Id
        note_value['Id'] = Id
        note_value['favorited'] = favorited
        note_value['favoriteCount'] = favoriteCount
        note_value['replyToSN'] = replyToSN
        note_value['replyToUID'] = replyToUID
        note_value['statusSource'] = statusSource
        note_value['screenNam'] = screenNam
        note_value['retweetCount'] = retweetCount
        note_value['isRetweet'] = isRetweet
        note_value['retweeted'] = retweeted
        note[Id] = note_value
        note_value = {}
#1
total_not_favorited = []
for val in note.values():
    if(val['favorited'] == 'FALSE'):
        print(val)
        total_not_favorited.append(val['Id'])
print("Total_not_favorited ==", len(total_not_favorited))

#2
total = []
for val in note.values():
    if(val['favoriteCount'] > 10 or val['favoriteCount'] > 50):
        print("favorite tweet count between 10 to 50 ==",val['favoriteCount'])
        total.append(val['favoriteCount'])
print("maximum favoritecount", max(total))

#3      
total1 = []
for val in note.values():
    if(val['favoriteCount'] > 0):
        total1.append(val['favoriteCount'])
print("minimum favoritecount", min(total1))

#4
total_peopel_replied = []
for val in note.values():
    if(val['replyToUID'] != 'NA'):
        print(val['replyToUID'])
        total_peopel_replied.append(val['Id'])
print("no of people replied ==", len(total_peopel_replied))

total_peopel_replied1 = []
for val in note.values():
    if(val['replyToUID'] == 'NA'):
        total_peopel_replied1.append(val['Id'])
print("no of people not replied ==", len(total_peopel_replied1))


#5
for val in note.values():
    if(val['screenNam'].endswith("p")):
        print("Screen name end with p ",val['screenNam'])

for val in note.values():
    if(val['screenNam'].startswith("D") or val['screenNam'].startswith("d")):
        print("Screen name start with D ",val['screenNam'])


#6
Sum = 0
avg = 0
retweet = []
for val in note.values():
    if(val['retweetCount']>0):
        Sum = Sum + val['retweetCount']
        retweet.append(val['retweetCount'])

avg = Sum/len(note)

print("maximum retweetCount = ", max(retweet))
print("minimum favoritecount = ", min(retweet))
print("overall retweet = ", Sum)
print("avrage retweetCount = ", avg)


        

