# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

# This censor should replace any appearance of "learning algorithms"
def censor_one(email, term = "learning algorithms"):
new_email = email
new_email = new_email.replace(term, "[CENSORED]")
return new_email

# This censor should replace any term from proprietary_terms
def censor_two(email, terms):
new_email = email
for term in terms:
  new_email = new_email.replace(term, "[CENSORED]")
return new_email

# This censor should replace any word from negative_words but first word appearance
def censor_three(email, words):
new_email = email.replace("\n\n", "*")
new_email = new_email.split()
new_email_lower = [i.lower() for i in new_email]
first_word_index = len(new_email)
temp_index = 0
for word in words:
  if word in new_email_lower:
    temp_index = new_email_lower.index(word)
    if temp_index < first_word_index:
      first_word_index = temp_index
for word in words:
  if word in new_email_lower:
    if new_email_lower.index(word) != first_word_index:
      new_email[new_email_lower.index(word)] = "[CENSORED]"
new_email = " ".join(new_email)
new_email = new_email.replace("*", "\n\n")
return new_email

# This censor should replace any word/term from both proprietary_terms and negative_words and the terms after and before.
def censor_four(email, words, terms):
  new_email = email.replace("\n\n", "*")
  new_email = new_email.split()
  new_email_lower = [i.lower() for i in new_email]
  for word in words:
    if word in new_email_lower:
      new_email[new_email_lower.index(word)] = "[CENSORED]"
      new_email[new_email_lower.index(word) - 1] = "[CENSORED]"
      new_email[new_email_lower.index(word) + 1] = "[CENSORED]"
  for term in terms:
    if term in new_email_lower:
      new_email[new_email_lower.index(term)] = "[CENSORED]"
      new_email[new_email_lower.index(term) - 1] = "[CENSORED]"
      new_email[new_email_lower.index(term) + 1] = "[CENSORED]"
  new_email = " ".join(new_email)
  new_email = new_email.replace("*", "\n\n")
  return new_email

#print(censor_one(email_one))
#print(censor_two(email_two, proprietary_terms))
#print(censor_three(email_three, negative_words))
#print(censor_four(email_four, negative_words, proprietary_terms))
