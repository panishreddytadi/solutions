students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

# Extract all scores
scores = sorted({s[1] for s in students})

# Second lowest score
second_lowest = scores[1]

# Get names of students with second lowest score
result = sorted([s[0] for s in students if s[1] == second_lowest])

# Print each name
for name in result:
    print(name)
