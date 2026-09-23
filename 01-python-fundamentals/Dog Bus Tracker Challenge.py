# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#
# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# 5. Print a final roster listing the remaining pets and their dropoff times.  

current_passengers = {
  '1': {'name': 'Rover', 'breed': 'Dalmatian', 'pickup_time': '8:00am', 'dropoff_time': '4:00pm'},
  '2': {'name': 'Chris', 'breed': 'Pomerian', 'pickup_time': '9:00am', 'dropoff_time': '4:45pm'},
  '3': {'name': 'Filo', 'breed': 'Finnish Laphund', 'pickup_time': '8:30am', 'dropoff_time': '4:30pm'},
  '4': {'name': 'Ruff', 'breed': 'Golden', 'pickup_time': '8:15am', 'dropoff_time': '4:15pm'},
  '5': {'name': 'WishItWasACat', 'breed': 'NotACat', 'pickup_time': '8:45am', 'dropoff_time': '5:00pm'},
}

for key, value in current_passengers.items():
  print(f'Seat #{key}: pickup {value["name"]} at {value["pickup_time"]}.')

max_seats = 6
if len(current_passengers) < max_seats:
  new_passenger = input('Enter the name of the new dog: ')
  new_breed = input('Enter the breed of the new dog: ')
  new_pickup_time = input('Enter the pickup time of the new dog: ')
  new_dropoff_time = input('Enter the dropoff time of the new dog: ')
  next_seat_number = str(len(current_passengers) + 1)
  current_passengers[next_seat_number] = {
    'name': new_passenger,
    'breed': new_breed,
    'pickup_time': new_pickup_time,
    'dropoff_time': new_dropoff_time
  }

for key, value in current_passengers.items():
  print(f'Seat #{key}: pickup {value["name"]} at {value["pickup_time"]}.')

while True:
  left_early = input('Enter the name of the dog that left early. Enter done to exit.')
  for key, value in current_passengers.items():
    if left_early == value['name']:
      del current_passengers[key]
    elif left_early == 'done':
      break
    else:
        print('That dog is not on the bus.')

for key, value in current_passengers.items():
  print(f'Seat #{key}: pickup {value["name"]} at {value["pickup_time"]}.')