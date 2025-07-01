def find_acronym():
    look_up = input('what software acronym would you like to look up?\n')

    found = False
    with open('acronyms.txt') as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break

    if not found:
        print('The acronym does not exist')

def aad_acronym():
    acronym = input('what acronym do you want to add?\n')
    definition = input('what is the definition?\n')
    with open('acronyms.txt', 'a') as file:
     file.write(acronym + '-' + definition + '\n')
