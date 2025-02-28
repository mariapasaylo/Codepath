#U
# function: parapemeter tasks a dictionary: key: task name and value: priority (1-10)
# return task with highest priority, if same then in alphabet order
# remove the task with highest priority and return it


#M
# maximum number

#P
# max(tasks) -> list[highest_keys]
# sort the list
# pop the first item in the task from the dict of the first item
# return task


#I
def get_highest_priority_task(tasks):
	max_value = max(tasks.values())
	key_to_remove = 0
	for key,value in tasks.items():
		if value == max_value:
			key_to_remove = key
			break
	tasks.pop(key_to_remove)
	return key_to_remove
	
	
	

#Test
tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)