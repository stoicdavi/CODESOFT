import random as rm
import string as st
PASS_FILE = 'passwords.txt'
def generate_pass(Pass_length, lowercase=True, uppercase=True, punctuation_marks=True, numbers=True):
  
  """
  Generates a random password with the specified length and complexity.
  """
  pass_chars = []


  if lowercase:
    pass_chars.extend(st.ascii_lowercase)
  if uppercase:
    pass_chars.extend(st.ascii_uppercase)
  if punctuation_marks:
    pass_chars.extend(st.punctuation)
  if numbers:
    pass_chars.extend(st.digits)

  password = ''.join(rm.choices(pass_chars,k=Pass_length))
  print(f'Your generated password is {password}')
  return password

def capture_user_input():
  while True:
    try:
      Pass_length = int(input("Enter the password length: "))
      if Pass_length <= 0:
        print('Invalid input! Please enter a positive number')
        continue
      break
    except ValueError:
      print('Invalid input! Please enter a positive number')

  lowercase_input = input("Incude lowercase? (yes or no): ").lower().strip()
  if lowercase_input in ['yes', 'y']:
    lowercase = True
  else:
    lowercase = False
  uppercase_input = input("Incude uppercase letters? (yes or no): ").lower().strip()
  if uppercase_input in ['yes', 'y']:
    uppercase = True
  else:
    uppercase = False
  Punctuation_input = input("Incude punctuation marks? (yes or no): ").lower().strip()
  if Punctuation_input in ['yes', 'y']:
    punctuation_marks = True
  else:
    punctuation_marks = False
  numbers_input = input("Incude numbers? (yes or no): ").lower().strip()
  if numbers_input in ['yes', 'y']:
    numbers = True
  else:
    numbers = False

  return Pass_length, lowercase, uppercase, punctuation_marks, numbers
def password_strength(password):
  length = len(password)
  has_upper = any(c.isupper() for c in password)
  has_lower = any(c.islower() for c in password)
  has_digit = any(c.isdigit() for c in password)
  has_punct = any(c in st.punctuation for c in password)
    
  strength = sum([length >= 8, has_upper, has_lower, has_digit, has_punct])   
  if strength <= 2:
    return "Weak"
  elif strength == 3:
   return "Moderate"
  else:
   return "Strong"

def save_password(password):
  with open(PASS_FILE, 'a') as rf:
    rf.write(password + '\n')
  print('Password saved to passwords.txt')

def read_passwords():
  with open(PASS_FILE, 'r') as rf:
    print(rf.read())

def delete_passwords():
  with open(PASS_FILE, 'w') as rf:
    choice = input('Are you sure you want to delete all passwords? (yes or no): ').lower()
    if choice in ['yes', 'y']:
      rf.write('')
    else:
      print('No passwords were deleted')

def main():
  print("**** Welcome to DeANTECH Random Password Generator ****\n")
  while True:
    print("Select:\n1. Generate a new password\n2. View generated passwords\n3. Delete all passwords\n0. Exit\n")
    try:
      selection = int(input("Choice: "))
      if selection == 1:
        Pass_length, lowercase, uppercase, punctuation_marks, numbers = capture_user_input()
        password = generate_pass(Pass_length, lowercase, uppercase, punctuation_marks, numbers)
        strength = password_strength(password)
        print(f'Password strength: {strength}')
        save_password(password)
      elif selection == 2:
        print('The Generated passwords are:')
        read_passwords()
      elif selection == 3:
        delete_passwords()
      elif selection == 0:
        break
      else:
        print("Invalid choice, please select a valid option.")
    except ValueError:
        print("Invalid input, please enter a number.")
    
  print("Thank you for using our password generator. Keep your passwords safe!")

if __name__ == '__main__':
    main()