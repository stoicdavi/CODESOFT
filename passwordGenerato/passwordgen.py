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

  lowercase_input = input("Do you want to incude lowercase? (yes or no): ").lower()
  if lowercase_input in ['yes', 'y']:
    lowercase = True
  else:
    lowercase = False
  uppercase_input = input("Do you want to incude uppercase letters? (yes or no): ").lower()
  if uppercase_input in ['yes', 'y']:
    uppercase = True
  else:
    uppercase = False
  Punctuation_input = input("Do you want to incude punctuation marks? (yes or no): ").lower()
  if Punctuation_input in ['yes', 'y']:
    punctuation_marks = True
  else:
    punctuation_marks = False
  numbers_input = input("Do you want to incude numbers? (yes or no): ").lower()
  if numbers_input in ['yes', 'y']:
    numbers = True
  else:
    numbers = False

  return Pass_length, lowercase, uppercase, punctuation_marks, numbers

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
  print("****Welcome to DeANTECH random password generator****\n")
  while True:
    print("Select:\n1.To generate a new password\n2.To view the generate passwords\n3.To Delete all the passwords\n0.To exit\n")
    selection = int(input("Choice: "))
    if selection == 1:
      Pass_length, lowercase, uppercase, punctuation_marks, numbers = capture_user_input()
      password = generate_pass(Pass_length,lowercase, uppercase,punctuation_marks,numbers)
      save_password(password)
      choice = input("\nDo you want to generate another password? (yes or no): ").lower()
      if choice not in ['yes', 'y']:
        break
    elif selection == 2:
       print('The Generated passwords are')
       read_passwords()
    elif selection == 3:
      delete_passwords()
      print('All passwords deleted')
    elif selection == 0:
      break
  
  print("Thank you for using our password generator \n\tMake sure to keep your passwords safe!")

if __name__ == '__main__':
  main()