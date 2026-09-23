# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

phone_number = input("Please enter a 10 digit phone number.").strip().replace("-"," ").replace("("," ").replace(")"," ").replace("."," ").split()
phone_number = ''.join(phone_number)
if len(phone_number) == 10:
    print(f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}")
else:
    print("Please enter exactly 10 digits.")