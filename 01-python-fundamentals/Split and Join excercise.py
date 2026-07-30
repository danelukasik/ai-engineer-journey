
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
friends_list.clear()
csv1 = csv.replace(":",",")
csv2 = csv1.replace(";",",")
friends_list.extend(csv2.split(","))
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

