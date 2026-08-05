# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revoked_badge_nums = {'00045','00700','12345','54321','75542','00354','48610','00454'}
approved = []
denied = []

while True:
  name = input('Enter your name. Enter \'done\' to exit.').title()
  if name == 'done':
    print('Access Summary')
    print('')
    print('✅ Approved Visitors')
    print(len(approved))
    print(sorted(approved))
    print('')
    print('⛔️ Denied Visitors')
    print(len(denied))
    print(sorted(denied))
    break
  else:
    badge_input = input('Enter you badge number.')
    if badge_input in revoked_badge_nums:
      denied.append(name)
      print("ACCESS DENIED")
    else:
      approved.append(name)
      print('ACCESS GRANTED')