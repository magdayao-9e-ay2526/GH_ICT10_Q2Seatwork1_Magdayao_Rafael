# Candidate verfication system
from pyscript import display, document


def view_member(e):
    document.getElementById('result').innerHTML = ' '
    student_first = document.getElementById('firstname').value
    student_last = document.getElementById('lastname').value

    student_name = str(student_first) + " " + str(student_last)

    Glee_members = ['Jalanie Abdullah', 'Clara Sabanal', 'Alexa Salcedo', 'Rafael Magdayao', 'Julianne Canuday', 'Theos Tomas', 'Amanda Bower',]
    member_checker = student_name in Glee_members # checks boolean 0 or 1

    display_message = (f'Sorry, you are not included in Glee club', f'Congratulations {student_name}, you are part of Glee club')
    display(display_message[member_checker], target='result') 