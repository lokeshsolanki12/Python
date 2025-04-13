'''
Q1 Manage a TO DO list'''
# Create a TO Do List to keep track of tasks

to_do_list = ["Buy Groceries", "Clean The House", "pay bills"]

# Adding the Tasks
to_do_list.append("schedule meating")
to_do_list.append("Go for a run")

# Remove the Task
to_do_list.remove("Clean The House")

#cheaking if a task is in the list

if "pay bills" in to_do_list:
    print("Yure payment is left")
print("TO DO list raimains")

for task in to_do_list:
    print(f"-{task}")
    

'''
Q2 Organizing student Grades'''

grades = [85,65,96,98,45,88]

# Add grade
grades.append(99)

#Average of grade

average_grade = sum(grades)/len(grades)
print(f"Average Grade:- {average_grade:.2f}")

#Find the highest and lowest Grade

highest_grade = max(grades)
lowest_grade = min(grades)

print(f"Highest Grade:- {highest_grade}")
print(f"Lowest Grade:- {lowest_grade}")