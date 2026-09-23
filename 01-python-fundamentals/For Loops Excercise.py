names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names_list = [names.title() for names in names] + [names1.title() for names1 in names1]

for num in [1,2]:
    names_list.extend([input("Enter a new name.")])

for name in names_list:
    print(f"{name.title()}! You are invited to the party on Saturday!")