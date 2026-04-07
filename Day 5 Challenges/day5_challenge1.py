tasks = ["Email client", "Call boss", "Fix bug"]
tasks.insert(3,"Lunch break")
tasks.insert(0, "Urgent meeting")
tasks.remove("Call boss")
sorted_tasks= sorted(tasks)
print(sorted_tasks)