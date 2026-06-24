# Job Scheduling using Backtracking

# List of jobs
jobs = ["J1", "J2", "J3"]

# List of employees
employees = ["E1", "E2", "E3"]

# Stores final job assignments
assignments = {}

# Stores employees already assigned a job
employee_busy = set()

def schedule_jobs(job_index):

    # Base Case:
    # If all jobs are assigned, solution is found
    if job_index == len(jobs):
        return True

    # Select current job
    current_job = jobs[job_index]

    # Try assigning current job to each employee
    for employee in employees:

        # Check whether employee is free
        if employee not in employee_busy:

            # Assign job to employee
            assignments[current_job] = employee

            # Mark employee as busy
            employee_busy.add(employee)

            # Recursively assign next job
            if schedule_jobs(job_index + 1):
                return True

            # Backtracking:
            # Remove assignment and try another employee
            del assignments[current_job]
            employee_busy.remove(employee)

    # No valid assignment found
    return False

# Start scheduling from first job
if schedule_jobs(0):

    print("Job Schedule Found:\n")

    # Display final schedule
    for job, employee in assignments.items():
        print(job, "-->", employee)

else:
    print("No feasible schedule found.")
