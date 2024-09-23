class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit

def find_slot(slot, parent):
    if parent[slot] == slot:
        return slot
    parent[slot] = find_slot(parent[slot], parent)
    return parent[slot]

def union_slot(u, v, parent):
    parent[u] = v

def job_sequencing(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    parent = [i for i in range(n + 1)]
    total_profit = 0
    job_sequence = []

    for job in jobs:
        available_slot = find_slot(min(job.deadline, n), parent)
        if available_slot > 0:
            job_sequence.append(job.id)
            total_profit += job.profit
            union_slot(available_slot, available_slot - 1, parent)

    if job_sequence:
        print("Job sequence:", ' '.join(map(str, job_sequence)))
        print(f"Total Profit: {total_profit}")
    else:
        print("No jobs could be scheduled.")

if __name__ == "__main__":
    num_jobs = int(input("Enter the number of jobs: "))
    if num_jobs <= 0:
        print("Invalid number of jobs.")
        exit(0)

    n = int(input("Enter the number of available slots: "))
    if n <= 0:
        print("Invalid number of available slots.")
        exit(0)

    jobs = []
    for i in range(num_jobs):
        job_id, deadline, profit = map(int, input(f"Enter job ID, deadline, and profit for job {i + 1}: ").split())
        if job_id <= 0 or deadline <= 0 or profit < 0:
            print(f"Invalid input for job {i + 1}. Please enter positive values.")
            exit(0)
        jobs.append(Job(job_id, deadline, profit))

    job_sequencing(jobs, n)
