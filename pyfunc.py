# pyfunc
# python librery
# MDRA.pyprogramer

from tabulate import tabulate
import sqlite3
import random
import webbrowser

def type_word(number = 1,word = None):
    a = 0
    while a < number :
        print(word)
        a += 1

def type_Divisible(c = 10,b = 100):
    for a in range(b + 1) :
        if a % c == 0:
            print(a, end = ' * ')
    
def type_not_Divisible(b = 10,c = 100):
    for a in range(b + 1) :
        if a % c != 0:
            print(a)

def search(searchweb):
    url = f'google.com/search?q={searchweb}'
    webbrowser.open(url)


def ggtn():
    while True:

        number1 = random.randint(1,100)

        while True:
            number2 = int(input('Guess the secret number'))

            if number1 < number2:
                print('The larger the number')

            elif number2 < number1:
                print('The number is smaller')

            elif number1 == number2:
                print('Well done, you guessed right')
                break

def Dice():
    '''doc string :
    Asks the user if the user says "y" or says "yes"
     (he\she) rolls the dice and says the result'''
    min = 1
    max = 6
    roll_agne = 'y'

    while roll_agne == 'y' or roll_agne == 'yes':
        print()
        print(random.randint(min,max))
        print()
        roll_agne = input('Do I roll the dice ? ')

def Prime_number(number : int):
    a = True

    for i in range(1, number):
        if number % i == 0 :
            if i != 1 and 0 :
                print(f'bar {i} bakhsh pazir ast')
                a = False

    if a == True :
        print(f'{number} is : Prime number')

class sqlitefunc:
    def __init__(self, file_db):

        conn = sqlite3.connect(file_db)
        self.c = conn.cursor()

    def create_table(self, name, *arge):

        'get table name and culems name'

        self.c.execute(f'''CREATE TABLE IF NOT EXISTS {name} {arge} ''')

    def insert(self, *arge, tablename):

        'get values for adding in sql'

        if len(arge) == 1:
            self.c.execute(f'INSERT INTO {tablename} VALUE {arge}')
        elif len(arge) > 1 :
            self.c.execute(f'INSERT INTO {tablename} VALUES {arge}')

    def select(self, tablename = '',**kwargs):

        a = ''

        for i in list(kwargs.keys()):
            if i != list(kwargs.keys())[len(list(kwargs.keys())) - 1]:
                value = '{} = ({}) AND'.format(i, kwargs.get(i))
                a + value
            
            elif i == list(kwargs.keys())[len(list(kwargs.keys())) - 1]:
                value = '{} = ({})'.format(i, kwargs.get(i))
                a + value

        self.c.execute(f'SELECT * FROM {tablename} WHERE {a}')

        value = self.c.fetchall()

        return tabulate(value)

    def select_all(self, tablename):
        self.c.execute(f'SELECT * FROM {tablename}')
        return tabulate(self.c.fetchall())

    def search(self, tablename, value):
        self.c.execute(f'SELECT * FROM {tablename} ')

        my_v = self.c.fetchall()
        for i in my_v:
            for a in i :
                for b in a :
                    if b in value:
                        return tabulate(a)

    def update(self, tablename, seter, **where):

        'give the (variable_setter, value_setter, variable_where, value_where) , python updateing the database'

        if type(seter) != dict:
            seter = {seter : None}

        a = ''

        for i in list(seter.keys()):
            if i != list(seter.keys())[len(list(seter.keys())) - 1]:
                value = f'{i} = ({seter.get(i)}) AND'
                a + value
            elif i == list(seter.keys())[len(list(seter.keys())) - 1]:
                value = f'{i} = ({seter.get(i)})'
                a + value            



        b = ''

        for i in list(where.keys()):
            if i != list(where.keys())[len(list(where.keys())) - 1]:
                value = f'{i} = ({where.get(i)}) AND'
                b + value
            elif i == list(where.keys())[len(list(where.keys())) - 1]:
                value = f'{i} = ({where.get(i)})'
                b + value


        self.c.execute(f'''UPDATE {tablename} SET {a} WHERE {b}''')

    def delete(self, tablename, **kwargs):

        'give the str is : variable and value'

        a = ''

        for i in list(kwargs.keys()):
            if i != list(kwargs.keys())[len(list(kwargs.keys())) - 1]:
                value = f'{i} = ({kwargs}) AND'
                a + value
            
            elif i == list(kwargs.keys())[len(list(kwargs.keys())) - 1]:
                value = f'{i} = ({kwargs})'
                a + value

        self.c.execute(f'''DELETE FROM {tablename} WHERE {a}''')

    def help():
        text_help = '''give the table and a list value and database file
        You can do 4 actions on your table and values where the database file is
        '''

        help_text = '''List of given values Each value is entered into the database as a separate variable
        give the variable first , then value , python searching in database
        give the (variable_setter, value_setter, variable_where, value_where) , python updateing the database
        Give the string (variable and value)'''

        return text_help, help_text
