string_length = len("Hello World!")
print(string_length)

name = "Tommy"
potatoes = 4.75
prompt = f"""Write a couplet about my friend {name} who has about {round(potatoes)} potatoes"""
response = get_llm_response(prompt)
print(response)


# Enter one of your favorite numbers. Multiply the result by 10 and save it to a variable called 'lucky_number'.
# Print a message saying "Your lucky number is [lucky_number]!"
 
Lucky_number = 3*10
print(f"Your lucky number is {Lucky_number}!")

# Use print_llm_response() to print a poem with the specified number of lines. Use the 
# prompt variable to save your prompt before calling print_llm_response()

number_of_lines = "12"
prompt = f"How many number_of_lines in the peom"
print_llm_response(prompt)


# Repeat exercise 2, this time using the function get_llm_response(), then print() to print it. This function asks 
# the LLM for a response, just like print_llm_response, but does not print it. You'll need to save the response to
# a variable, then print it out separately.

number_of_lines = 10
prompt = f"How many number_of_lines in the peom"
response = get_llm_response(prompt)
print(response)
