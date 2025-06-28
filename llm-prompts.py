from helper_functions import print_llm_response #type: ignore

print_llm_response("What is the capital of France?")

name = "Otto Matic"
dog_age = 23/7

print_llm_response(f"""If {name} were a dog, he would be {dog_age} years old.
Describe what life stage that would be for a dog and what that might 
entail in terms of energy level, interests, and behavior.""")
