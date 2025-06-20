student_score = {
    "Alice" : 85,
    "Bob" : 92,
    "Charlie":78,
    "David" : 95,
    "Eve" : 88,
    "Frank" : 70

}
    
print("initial Student Scores")

for name,score in student_score.items():
    print (f"{name}:{score}")
print("\n")

student_score["Muhaimin"] = 100
print("updated list :")
for name,score in student_score.items():
    print (f"{name}:{score}")
print("\n")



