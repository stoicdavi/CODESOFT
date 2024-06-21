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
  print(pass_chars)
  print(password)

generate_pass(6,0,0,4,4)