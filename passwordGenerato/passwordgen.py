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
  print(password)

def capture_user_input():
  while True:
    print("Hello welcome")
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

  return Pass_length, lowercase

def main():
  print("****Welcome our random password generator****")
  Pass_length, lowercase = capture_user_input()
  
  generate_pass(Pass_length,lowercase,0,4,4)

if __name__ == '__main__':
  main()