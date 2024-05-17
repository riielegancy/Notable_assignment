
word_to_num ={'one' : 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def parse_transcribed_notes(text, word_to_num):
  
  """
  Transforms transcribed doctor's text with numbered list phrases into a formatted list.

  Args:
      text: The transcribed text string.

  Returns:
      The formatted text with numbered lists.
  """
  list_items = []
  current_number = 0
   
  for sentence in text.split('.'):
    sentence = sentence.strip()  
    print(sentence)
    # Handle "Number n" phrases (case-insensitive)
    if sentence.lower().startswith("number "):
      try:
        # Extract the number
        current_number = word_to_num[sentence.split()[1]]
        # Ensure number is within 1-9 range
        if not 1 <= current_number <= 9:
          raise ValueError("Invalid number (must be between 1 and 9)")
      except (IndexError, ValueError):
        # Ignore invalid number format or missing number
        continue

    # Handle "Number next" phrase (case-insensitive)
    elif sentence.lower() == "number next":
      current_number += 1  # Increment to the next item
  
    else:
      # Capitalize the first letter if not already capitalized (excluding articles)
      if sentence and not sentence[0].isupper() and sentence[0] not in ("a", "an", "the"):
        sentence = sentence.capitalize()

      # Add the formatted item to the list
      list_items.append(f"{current_number}. {sentence}")

  return "\n".join(list_items)

doctor_text = "Patient presents today with several issues. Number one BMI has increased by 10% since their last visit number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks Number next patient is taking drug number five several times a week"

formatted_text = parse_transcribed_notes(doctor_text, word_to_num)

print(formatted_text)