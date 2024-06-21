import random as rm
import string as st

def generate_pass(Pass_length, lowercase, uppercase, punctuation_marks, numbers):
  
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

  password = ''.join(pass_chars)
  print(pass_chars)
  print(password)

generate_pass(1,1,3,4,4)