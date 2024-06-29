import random as rm
import string as st

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
  with open('passwords.txt', 'a') as rf:
    rf.write(password + '\n')
  print('Password saved to passwords.txt')

def read_passwords():
  with open('passwords.txt', 'r') as rf:
    print(rf.read())


def main():
  while True:
    print("\n****Welcome our random password generator****\n")
    Pass_length, lowercase, uppercase, punctuation_marks, numbers = capture_user_input()
    password = generate_pass(Pass_length,lowercase, uppercase,punctuation_marks,numbers)
    save_password(password)
    choice = input("\nDo you want to generate another password? (yes or no): ").lower()
    if choice not in ['yes', 'y']:
      read_passwords()
      break
  
  print("Thank you for using our password generator")

if __name__ == '__main__':
  main()