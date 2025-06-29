contacts = {
    'number': 4,
    'students': [
        {'name': 'Shamserul', 'email': 'shamserul@gmail.com'},
        {'name': 'Maheen', 'email': 'maheen@gmail.com'},
        {'name': 'Ashriti', 'email': 'ashriti@gmail.com'},
        {'name': 'Khushboo', 'email': 'khushboo@gmail.com'}
    ]
}

print('students emails:')
for student in contacts['students']:
    print(student['email'])