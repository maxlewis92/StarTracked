import imdb
ia = imdb.IMDb()
movie = raw_input('What movie? ')
print("\nResults:")
result = ia.search_movie(movie)
for item in result:
    print(item['long imdb canonical title']+" | ID:"+ item.movieID)
print("\n\tIMDB ID of first result ("+result[0]['long imdb canonical title'] + "): "+result[0].movieID)
print("\n\nCast and Crew of "+result[0]['title']+" ")
givenID = result[0].movieID
givenObject = ia.get_movie(givenID)
ia.update(givenObject, 'full credits')
print(givenObject.keys())
print("\n\n")

print("Directors:")
for item in givenObject['director']:
    print("\t" + item['name'] + "\t\t  |  "+item.personID)

print("Producer:")
for item in givenObject['producer']:
    print("\t" + item['name'] + "\t\t  |  "+item.personID)

print("Writers:")
for item in givenObject['writer']:
    print("\t" + item['name'] + "\t\t  |  "+item.personID)
    
print("Cast:")
for item in givenObject['cast']:
    print("\t" + item['name'] + "\t\t  |  "+item.personID)
    
#print("Cast: "+result[0]['cast']['name'])

