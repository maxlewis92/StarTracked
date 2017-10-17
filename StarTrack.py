import imdb

searchTitle = "Star Trek"

def investigate(searchSubject):
    ia.update(searchSubject)
    #print(searchSubject.keys())
    #print("Investigating "+searchSubject['name'])
    if searchSubject.has_key("director"):
        for item in searchSubject['director']:
            #print("Directed:\t" + item['long imdb canonical title'])
            if searchTitle in item['long imdb canonical title']:
                print(searchSubject['name'] + " also directed " + item['long imdb canonical title'])
    if searchSubject.has_key("producer"):
        for item in searchSubject['producer']:
            #print("Produced:\t" + item['long imdb canonical title'])
            if searchTitle in item['long imdb canonical title']:
                print(searchSubject['name'] + " also produced " + item['long imdb canonical title'])
    if searchSubject.has_key("writer"):
        for item in searchSubject['writer']:
            #print("Wrote:\t\t" + item['long imdb canonical title'])     
            if searchTitle in item['long imdb canonical title']:
                print(searchSubject['name'] + " also wrote " + item['long imdb canonical title'])
    if searchSubject.has_key("actor"):
        for item in searchSubject['actor']:
            #print("Acted:\t\t" + item['long imdb canonical title'])
            if searchTitle in item['long imdb canonical title']:
                role = searchSubject['actor'][5].currentRole
                ia.update(role)
                print(searchSubject['name'] + " also played " + unicode(role) +" in" + item['long imdb canonical title'])
    if searchSubject.has_key("actress"):
        for item in searchSubject['actress']:
            #print("Acted:\t\t" + item['long imdb canonical title'])
            if searchTitle in item['long imdb canonical title']:
                role = searchSubject['actress'][0].currentRole
                print(searchSubject['name'] + " also played " + role +" in" + item['long imdb canonical title'])
                
ia = imdb.IMDb()
starTracked = False
movie = raw_input('What movie? ')

print("\nResults:")
result = ia.search_movie(movie)
i = 1
for item in result:
    #print("[" + str(i) + "]\t" + item['long imdb canonical title']+" | ID:"+ item.movieID)
    print("[" + str(i) + "]\t" + item['long imdb canonical title'])
    i+= 1
    
selection = int(input("\n\n\nEnter the item number of the movie\n"))

###I need data validation

selection -= 1

#print("\n\tIMDB ID of first result ("+result[selection]['long imdb canonical title'] + "): "+result[0].movieID)

givenID = result[0].movieID
givenObject = ia.get_movie(givenID)
ia.update(givenObject, 'full credits')
givenObject.keys()

print("\n\nSearching for connections, this may take a while...")

print("\n\nStar Trek Connections:")
if givenObject.has_key('director'):
    for item in givenObject['director']:
        #print("\t" + item['name'] + "\t\t  |  "+item.personID)
        activePerson = ia.get_person(item.personID)
        investigate(activePerson,starTracked)
if givenObject.has_key('producer'):
    for item in givenObject['producer']:
        #print("\t" + item['n#ame'] + "\t\t  |  "+item.personID)
        activePerson = ia.get_person(item.personID)
        investigate(activePerson,starTracked)
if givenObject.has_key('writer'):
    for item in givenObject['writer']:
        #print("\t" + item['name'] + "\t\t  |  "+item.personID)
        activePerson = ia.get_person(item.personID)
        investigate(activePerson,starTracked)
if givenObject.has_key('cast'):
    for item in givenObject['cast']:
        #print("\t" + item['name'] + "\t\t  |  "+item.personID)
        activePerson = ia.get_person(item.personID)
        investigate(activePerson,starTracked)

    
print("\n\nFinished.")