results = {
    'Maths': [87, 92, 78, 85, 90, 88, 76, 81, 95, 89],
    'Science': [80, 85, 82, 88, 91, 84, 79, 83, 87, 86],
    'English': [78, 82, 85, 88, 91, 84, 81, 79, 80, 86],
    'IT': [92, 88, 91, 87, 85, 89, 86, 83, 84, 90]
}

test_stats = {}
for subject, marks in results.items():
    test_stats[subject] = {
        'highest': max(marks),
        'lowest': min(marks),
        'average': sum(marks) / len(marks)
    }

all_marks = [mark for marks in results.values() for mark in marks]
overall_stats = {
    'highest': max(all_marks),
    'lowest': min(all_marks),
    'average': sum(all_marks) / len(all_marks)
}

print("Test Statistics:", test_stats)
print("Overall Statistics:", overall_stats)
