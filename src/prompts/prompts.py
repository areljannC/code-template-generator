from templates.frontEnd import *

OPTIONS = ['Front-End']

FRONT_END_OPTIONS = (
    'React Functional Component',
    'React w/ Redux boilerplate',
    'React w/ Styled Components',
    'React w/ Prop Types',
    'React w/ all'
)


def prompt():
    for i, option in enumerate(OPTIONS):
        print(f'{i}. {option}\n')

    option = int(input())

    if option == 0:
        frontEndPrompts()


def frontEndPrompts():
    for i, option in enumerate(FRONT_END_OPTIONS):
        print(f'{i}. {option}\n')

    option = int(input())

    if option == 0:
        print(REACT)
    elif option == 1:
        print(REACT_REDUX)
    elif option == 2:
        print(REACT_REDUX)
    elif option == 3:
        print(REACT_STYLED_COMPONENTS)
    elif option == 4:
        print(REACT_ALL)
