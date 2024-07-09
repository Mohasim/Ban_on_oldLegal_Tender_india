import sys

favorited = ""
favoriteCount = 0
replyToSN = ""
created = ""
Id = ""
replyToUID = ""
statusSource = ""
screenNam = ""
retweetCount= 0
isRetweet = ""
retweeted = ""

for line in sys.stdin:
    
    line = line.strip()

    columns = line.split(",")

    favorited = columns [0]
    favoriteCount = columns[1]
    replyToSN = columns[2]
    created = columns[3]
    Id = columns[6]
    replyToUID = columns[7]
    statusSource = columns[8]
    screenNam = columns[9]
    retweetCount= columns[10]
    isRetweet = columns[11]
    retweeted = columns[12]

    print(favorited+","+favoriteCount+","+replyToSN+","+created+","+Id+","+replyToUID+","+
          statusSource+","+screenNam+","+retweetCount+","+isRetweet+","+retweeted)




    
    
