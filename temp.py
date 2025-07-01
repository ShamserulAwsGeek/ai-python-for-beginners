#ask the user what acronym they want to add
acronym = input('What acronym do you want to add?\n')

#teh ask the user for the definition
definition = input('what is the definition?\n')

#open the file
with open('acronyms.txt', 'a') as file:
    file.write(acronym + '-' + definition + '\n')

#write the new acronym and definition to the file
