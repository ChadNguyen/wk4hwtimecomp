# question 1
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
# 3 months/ 4 quarters in a yr.

# O(1) because it is constant. The input will never exceed 1-12 so the runtime will be the same everytime.
def quarter_of(month):
    quarter = (month - 1) // 3 + 1
    return quarter

print(quarter_of(2)) # returns 1 for 1st quarter
print(quarter_of(6)) # returns 2 for 2nd quarter
print(quarter_of(9)) # returns 3 for 3rd quarter
print(quarter_of(11)) # returns 4 for 4th quarter

# question 2
# O(n) Linear Time
def final_grade(exam, projects):
    grade = 0
    if exam > 90 or projects > 10:
        grade = 100
    elif exam > 75 and projects >= 5:
        grade = 90
    elif exam > 50 and projects >= 2:
        grade = 75
    return grade


# question 3
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise

# O(n) iterates through the list once using a for loop same constant time
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    horizontal_blocks = 0
    vertical_blocks = 0
    
    for block in walk:
        if block == 'n':
            vertical_blocks += 1
        elif block=='s':
            vertical_blocks -= 1
        elif block == 'e':
            horizontal_blocks += 1
        elif block == 'w':
            horizontal_blocks -= 1
    
    return horizontal_blocks == 0 and vertical_blocks == 0



# question 3


