# I was supposed to put a comment here(NOTE: I left your comments in and add/fix to them, too. I hope that's okay?)
# My Last Name: Bullard

# CTI-110

# P3HW1 - Debugging

# Kelly Bullard

# October 24, 2022

#

# INFO: This program takes a number grade, processes and determines the average's letter grade.
# By it displaying letter grade for the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print('') # The in-between spaces

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: Determine lowest, highest, sum and average for grades
lowest = min(grades)
highest = max(grades)
sum_grades = sum(grades)
avg_grades = sum_grades/len(grades)

# Output
print('------------Results------------')
print(f'Lowest Grade:       {lowest:.1f}')
print(f'Highest Grade:      {highest:.1f}')
print(f'Sum of Grades:      {sum_grades:.1f}')
print(f'Average:            {avg_grades:.2f}')
print('-----------------------------------------')

# Determine letter grade for average

if avg_grades >= 90 and avg_grades <= 100:
  print('Your grade is: A')
elif avg_grades >= 80 and avg_grades <= 89:
  print('Your grade is: B')
elif avg_grades >= 70 and avg_grades <= 79:
  print('Your grade is: C')
elif avg_grades >= 60 and avg_grades <= 69:
  print('Your grade is: D')
else:
  print('Your grade is: F') # TO DO: Finish this






