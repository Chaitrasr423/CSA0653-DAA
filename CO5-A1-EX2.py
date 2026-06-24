# Exam Timetabling using Graph Coloring and Backtracking

# Exams
exams = ["E1", "E2", "E3", "E4"]

# Student conflicts between exams
# If two exams have common students, they cannot be scheduled together
graph = {
    "E1": ["E2", "E3"],
    "E2": ["E1", "E4"],
    "E3": ["E1", "E4"],
    "E4": ["E2", "E3"]
}

# Available time slots (colors)
time_slots = ["Slot1", "Slot2", "Slot3"]

# Stores exam -> assigned slot
schedule = {}

def is_safe(exam, slot):
    """
    Check whether assigning the slot to the exam
    creates a conflict with neighboring exams.
    """
    
    # Check all conflicting exams
    for neighbor in graph[exam]:
        
        # If neighbor already has same slot
        if neighbor in schedule and schedule[neighbor] == slot:
            return False

    return True


def timetable(exam_index):
    """
    Backtracking function to assign slots to exams.
    """

    # Base Case:
    # All exams are assigned
    if exam_index == len(exams):
        return True

    # Select current exam
    current_exam = exams[exam_index]

    # Try each available slot
    for slot in time_slots:

        # Constraint Check:
        # No conflicting exams should share same slot
        if is_safe(current_exam, slot):

            # Assign slot
            schedule[current_exam] = slot

            # Recursively assign next exam
            if timetable(exam_index + 1):
                return True

            # Backtracking:
            # Remove assignment if solution fails
            del schedule[current_exam]

    return False


# Start scheduling
if timetable(0):

    print("Exam Timetable:\n")

    for exam, slot in schedule.items():
        print(exam, "-->", slot)

else:
    print("No feasible timetable found.")
