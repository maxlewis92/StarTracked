import imdb

i = imdb.IMDb()

m = i.get_movie('0057012')
j = 0
for j in range(len(m['cast'])):
    ps = m['cast'][j]
    test = ps.currentRole
    print (unicode(ps.currentRole) + unicode(ps.keys()))
'''
p = i.get_person('0001715')
i.update(p)
if p.has_key("actor"):
        for item in p['actor']:
            #print("Acted:\t\t" + item['long imdb canonical title'])
            role1 = p['actor'][0].currentRole
            i.update(role1)
            print(role.keys())
            print(p['name'] + " also played " + unicode(role) +" in" + item['long imdb canonical title'])
  '''

person = i.get_person('0001715')
i.update(person)
actcredits = person['actor']
#i.update(actcredits)
j = 0
for j in range(len(person['actor'])):
    actcredits = person['actor'][j]
    print(unicode(actcredits.currentRole)+unicode(actcredits.keys()) + actcredits['title'])

print("Done")