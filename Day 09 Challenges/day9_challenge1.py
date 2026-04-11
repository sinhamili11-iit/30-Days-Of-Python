students = [{"name" : "A", "score" : 80,}, {"name" : "B", "score" : 70}, {"name" : "C", "score" : 95}, {"name" : "D", "score" : 92 }, {"name" : "E", "score" : 76}]
for student in students:
    if student["score"] > 80:
        print(student["name"])