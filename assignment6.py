def load_data_from_file(filename):
    countries = []
    with open(filename, 'r') as file:
        for line in file:
            countries.append(line.strip())
    return countries

def print_menu(options):
    print('----------------------------')
    for i in range(len(options)):
        print(f'{i + 1}. {options[i]}')

def get_choice(options):
    while True:
        choice = input('Please enter a choice: ')
        choice = choice.strip()
        if not choice.isnumeric():
            print('Choice must be a number')
        elif len(choice)>1 and choice[0]=='0':
            print ('Number which begins with 0 is not allowed')
        else:
            choice = int(choice)
            if 1 <= choice <= len(options):
                return choice
            else:
                print(f'Please choose a value between 1 and {len(options)}')

def find_country_by_name(countries):
    search_term = input('Please enter your search term: ')
    result_list = []

    for country in countries:
        if search_term in country:
            result_list.append(country)

    return result_list

def display_results(result_list):
    print(f'Found {len(result_list)} result(s)')
    for country in result_list:
        print(country)

def add_new_country(filename):
    countries = load_data_from_file(filename)
    new_country = input('Please enter the new country: ')

    if new_country in countries:
        print('Error: country exists')
    else:
        with open(filename, 'a') as file:
            file.write('\n' + new_country)
        print(f'Added {new_country}')

    return load_data_from_file(filename)

"""
DO NOT MODIFY ANYTHING BELOW THIS LINE
"""
def run():
    filename = 'data.txt'

    menu_options = [
        'List All Countries',
        'Search Country By Name',
        'Add New Country',
        'Quit'
    ]
    countries = load_data_from_file(filename)

    while True:
        print_menu(menu_options)

        choice = get_choice(menu_options)

        if choice == 1:
            print(*countries, sep='\n')
        elif choice == 2:
            display_results(find_country_by_name(countries))
        elif choice == 3:
            countries = add_new_country(filename)
        elif choice == 4:
            break
        else:
            print('Invalid menu choice')

    print('Goodbye')

run()