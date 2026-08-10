#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

department_store = {**freelancers, **antiques, **pet_shop}
#create an empty shopping cart
cart = {}
purse = 1000
print(f'Department Store inventory: {department_store}')
#loop through stores/dicts
for shop in [freelancers, antiques, pet_shop]:
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop.get("name")}! what do you want to buy: {list(shop.items())[1:]}? Type \'exit\' to leave without buying anything.')
    #update the cart
    if buy_item == "exit":
        print(f'You have exited {shop.get("name")} without buying anything.')
        continue
    elif buy_item not in shop:
        print(f'You cannot buy {buy_item} from {shop.get("name")}! You have been kicked out of the store!')
        continue
    cart.update({buy_item: shop.pop(buy_item)}) # use pop...

#while True:
    #buy_item = input(f'Welcome to the department store! What do you want to buy: {department_store.items()}? Type \'exit\' to leave without buying anything.')
    #update the cart
    #if buy_item == "exit":
        #print(f'You have exited the store without buying anything.')
        #break
    #elif buy_item not in department_store:
        #print(f'You cannot buy {buy_item}! You have been kicked out of the store!')
        #continue
    #cart.update({buy_item: department_store.pop(buy_item)}) # use pop...
department_store = {**freelancers, **antiques, **pet_shop}
purse -= sum(cart.values())
print(f'You Purchased {cart}. Today you have spent {sum(cart.values())} gold pieces. You have {purse} gold pieces left. Have a nice day of mayhem!')
print(f'Department Store inventory: {department_store}')