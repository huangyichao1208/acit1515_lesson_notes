from pathlib import Path
from random import randint


"""
Key Skills for Assignment 6:
    1. Creating a function
    2. Creating a function that accepts parameters
    3. Creating a function that returns a value
    4. Write to a file
    5. Read from a file
"""


"""
1. Creating Basic Functions
"""
def create_assignment_metadata():
    """
    PRACTICE 1: Create a function that creates a file named '.metadata' in the 
    current directory (use Path.cwd())
    """
    cwd = Path.cwd()
    file1 = cwd / '.metadata'
    file1.touch()
    pass

def initialize_workspace():
    """
    PRACTICE 2: Create a function that simulates setting up a workspace
    Should print:
    - Creating workspace...
    - Checking permissions...
    - Setup complete!
    """
    print ('Creating workspace...')
    print ('Checking permissions...')
    print ('Setup complete!')
    pass

def display_menu():
    """
    PRACTICE 3: Create a function that displays a menu of options from a list of strings
    using a for loop
    Should print:
    1. Create new assignment
    2. List assignments
    3. Exit
    """
    list_string = ['Create new assignment','List assignments','Exit']
    for menu in list_string:
        print (menu)
    pass

def prompt():
    """
    PRACTICE 4: Create a function that prompts a user for the following
    (numeric) values:
        - Year
        - Month
        - Day
        - Hour
        - Minute
    Should print "You entered: {year}-{month}-{day} {hour}:{minute}"
    """
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))
    print(f"You entered: {year}-{month}-{day} {hour}:{minute}")
    pass

def clear_screen():
    """
    PRACTICE 5: Create a function that simulates clearing the screen
    Should print 50 newline characters
    """
    for i in range (50):
        print ()
    pass


"""
2. Functions with Parameters
"""
def create_assignment_folder(number):
    """
    PRACTICE 1: Create a function that accepts an assignment number
    Should print: Creating assignment folder: assignment{number}
    
    Args:
        number: The assignment number to create
    """
    print (f'assignment{number}')
    pass

def validate_course_code(code, year):
    """
    PRACTICE 2: Create a function that validates a course code and year
    Should print: Validating {code} for year {year}
    
    Args:
        code: Course code (e.g., 'ACIT')
        year: Year to validate for
    """
    print (f'Validating {code} for year {year}')
    pass

def format_assignment_name(course, number, suffix = ""):
    """
    PRACTICE 3: Create a function with both required and optional parameters
    Should print: {course}_assignment_{number}{suffix}
    
    Args:
        course: Course code
        number: Assignment number
        suffix: Optional suffix (default empty string)
    """
    print (f'{course}_assignment{number}{suffix}')
    pass

def print_assignments(*assignments):
    """
    PRACTICE 4: Create a function that accepts a list with variable number of assignment names
    Should print each assignment name on a new line
    
    Args:
        *assignments: Variable number of assignment names
    """
    for assignment_name in assignments:
        print (assignment_name)
        
    pass

def format_assignment_details(assignment_name, **metadata):
    """
    PRACTICE 5: Create a function that formats assignment details using keyword arguments
    Should create a formatted string containing assignment details.
    Expected keyword arguments include: due_date, weight, format, submission_type
    
    Example:
        format_assignment_details("Assignment 6", 
                                   due_date = "Oct 31", 
                                   weight = 20, 
                                   format = ".py",
                                   submission_type = "github")
    Should return:
        "Assignment 6 | Due: Oct 31 | Weight: 20% | Format: PDF | Submit via: github"
    
    Args:
        assignment_name: Name of the assignment
        **metadata: Keyword arguments for assignment metadata, e.g.:
                   - due_date: When the assignment is due
                   - weight: Percentage weight of the assignment
                   - format: Required submission format
                   - submission_type: How to submit the assignment
    """
    due_date = metadata ['due_date']
    weight = metadata ['weight']
    format = metadata ['format']
    submission_type = metadata ['submission_type']
    result = f'{assignment_name} | Due: {due_date} | Weight: {weight}% | Format: {format} | Submit via: {submission_type}'
    return result
    pass


"""
3. Functions with Return Values
"""
def get_assignment_number():
    """
    PRACTICE 1: Create a function that returns an assignment number
    Should return a random number between 1 and 10
    
    Returns:
        int: Random assignment number
    """
    next_num = randint(1,10)
    return next_num
    pass

def is_valid_course_folder(path):
    """
    PRACTICE 2: Create a function that validates a course folder path
    (as a string, not a Path object)
    Should return True if path contains 'BCIT', False otherwise
    
    Args:
        path: String path to validate
    Returns:
        bool: True if valid, False otherwise
    """
    if 'BCIT' in path:
        return True
    else:
        return False
    pass

def calculate_average_grade(grades):
    """
    PRACTICE 3: Create a function that calculates average grade
    Should return the average of all numbers in the list
    
    Args:
        grades: List of numeric grades
    Returns:
        float: Average grade
    """
    sum = 0
    avg=0
    for i in range (len(grades)):
        sum = sum + grades [i]
    avg = float (sum / (len(grades)))
    return avg
    pass

def generate_assignment_path(course, number: int) -> str:
    """
    PRACTICE 4: Create a function that generates an assignment path
    Should return: f"/home/student/Documents/{course}/assignment{number}"
    
    Args:
        course: Course number
        number: Assignment number
    Returns:
        str: Generated path
    """
    assignment_path = f'/home/student/Documents/{course}/assignment{number}'
    return assignment_path
    pass

def parse_assignment_name(filename):
    """
    PRACTICE 5: Create a function that parses an assignment filename
    using slice notation
    Should return tuple of (course_code, assignment_number)
    Example: "ACIT1515_assignment_6.py" -> ("ACIT1515", 6)
    
    Args:
        filename: Assignment filename to parse
    Returns:
        tuple: (course_code, assignment_number)
    """
    course_code = filename [0:8]
    assignment_number = filename [20]
    file_tuple = (f'{course_code}', assignment_number)
    return file_tuple
    pass

"""
4. Writing to a file
"""
def write_to_file(filename):
    """
    PRACTICE 1: Pass the filename parameter to the open() function
    and write a string of your choice to the file. Ensure that the
    string contains a terminating newline character '\n'
    
    Args:
        filename: The name of the file to be created
    Returns:
        None
    """
    with open(filename,'w') as file:
        file.write ("hello world\n")
    pass

def append_to_file(filename):
    """
    PRACTICE 2: Pass the filename parameter to the open() function
    and write a string of your choice to the file, ensuring that the
    existing contents of the file are not overwritten. Ensure that the
    string contains a terminating newline character '\n'
    
    Args:
        filename: The name of the file to be created
    Returns:
        None
    """
    with open (filename , 'a') as file:
        file.write ("11\n")
    pass

"""
5. Reading from a file
"""
def read_from_file(filename):
    """
    PRACTICE 1: Pass the filename parameter to the open() function
    and read the contents of the file (using any of the techniques
    discussed in class). Once the file contents have been read, return
    them as a string

    Args:
        filename: The name of the file to be opened
    Returns
        string: The contents of the file
    """
    with open (filename, 'r') as file:
        file_content = ''
        for content in file:
            file_content= file_content + content.strip
    return file_content
    pass

if __name__ == "__main__":
    # Test basic functions
    print("\nTesting basic functions:")
    create_assignment_metadata()
    initialize_workspace()
    display_menu()
    prompt()
    clear_screen()
    
    # Test functions with parameters
    print("\nTesting functions with parameters:")
    create_assignment_folder(6)
    validate_course_code("ACIT", 2505)
    format_assignment_name("ACIT1515", 6, "_final")
    print_assignments("assignment1", "assignment2", "assignment3")
    formatted = format_assignment_details("Assignment 6", due_date="Oct 31", weight=20, format="pdf", submission_type="github")
    print(f"Formatted details: {formatted}")
    
    # Test functions with return values
    print("\nTesting functions with return values:")
    next_num = get_assignment_number()
    print(f"Next assignment number: {next_num}")
    
    is_valid = is_valid_course_folder("/home/student/BCIT/ACIT1515")
    print(f"Is valid course folder: {is_valid}")
    
    avg = calculate_average_grade([85, 90, 95])
    print(f"Average grade: {avg}")
    
    path = generate_assignment_path("ACIT1515", 6)
    print(f"Generated path: {path}")
    
    course, number = parse_assignment_name("ACIT1515_assignment_6.py")
    print(f"Parsed filename: Course={course}, Number={number}")

    # add additional tests below for parts 4 and 5
    