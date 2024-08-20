# Exercise 1: Vowel or Consonant

# def check_letter():
#     while True:
#         letter = input('Enter a letter (a-z or A-Z): ').lower()
#         vowels = ['a', 'e', 'i', 'o', 'u']

#         if not letter.isalpha() or len(letter) > 1:
#             print(f'"{letter}" is not a valid input. Please try again')
#         elif letter in vowels:
#             print(f'The letter "{letter}" is a vowel.')
#             break
#         else:
#             print(f'The letter "{letter}" is a consonant.')
#             break

# check_letter()


# Exercise 2: Old enough to vote?

# def check_voting_eligibility():
#     LEGAL_VOTING_AGE = 18

#     while True:
#         age = input("Please enter your age: ")

#         if not age.isnumeric() :
#             print(f'"{age}" is not a valid input. Please try again')
#         elif int(age) < LEGAL_VOTING_AGE:
#             print(f'"{int(age)}" is not a legal voting age.')
#             break
#         else:
#             print(f'"{int(age)}" is a legal voting age.')
#             break

#     # Call the function
# check_voting_eligibility()


# Exercise 3: Calculate Dog Years

# def calculate_dog_years():
#     while True:
#         human_dog_age = int(input("Input a dog's age: "))

#         if human_dog_age < 0:
#             print(f'"{human_dog_age}" is not a valid input. Please try again')
#             continue
#         elif human_dog_age <= 2:
#             dog_years = human_dog_age * 10
#             print(dog_years)
#         elif human_dog_age > 2:
#             dog_years = 20 + (human_dog_age - 2) * 7
#             print(dog_years)
#         break

# calculate_dog_years()


# Exercise 4: Weather Advice

# def weather_advice():
#     is_cold = input('Is it cold outside? (Y/N): ').lower()
#     is_raining = input('Is it raining outside? (Y/N): ').lower()

#     is_cold = True if is_cold == 'y' else False
#     is_raining = True if is_raining == 'y' else False


#     if is_cold and is_raining:
#         print("Wear a waterproof coat.")
#     elif is_cold and not is_raining:
#         print("Wear a warm coat.")
#     elif not is_cold and is_raining:
#         print("Carry an umbrella.")
#     else:
#         print("Wear light clothing.")

# weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
              'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    month = input("Enter the month of the year (mmm): ").lower()
    try:
        day = int(input("Enter the day of the month (dd): "))
    except ValueError:
        print("Invalid day. Please enter a valid day number.")
        return
    
    
    if (month == 'dec' and day >= 21) or (month == 'jan' or month == 'feb') or (month == 'mar' and day <= 19):
        print('Winter')
    elif (month == 'mar' and day >= 20) or (month == 'apr' or month == 'may') or (month == 'jun' and day <= 20):
        print('Spring')
    elif (month == 'jun' and day >= 21) or (month == 'jul' or month == 'aug') or (month == 'sep' and day <= 21):
        print('Summer')
    elif (month == 'sep' and day >= 22) or (month == 'oct' or month == 'nov') or (month == 'dec' and day <= 20):
        print('Fall')
    else:
        print('Invalid input. Please try again')
determine_season()
