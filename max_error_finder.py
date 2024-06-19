from collections import Counter

# Read the log file
with open('FileHandling/logfile.txt', 'r') as file:
    log_lines = file.readlines()

# Initialize counters
error_counter = Counter()
info_counter = Counter()
warn_counter = Counter()

# Process each line in the log file
for line in log_lines:
    if ' - ERROR - ' in line:
        error_type = line.split(' - ERROR - ')[1].strip()
        print(error_type)
        error_counter[error_type] += 1
        print(error_counter)
    elif ' - INFO - ' in line:
        info_type = line.split(' - INFO - ')[1].strip()
        info_counter[info_type] += 1
    elif ' - WARN - ' in line:
        warn_type = line.split(' - WARN - ')[1].strip()
        warn_counter[warn_type] += 1

# Get the most common error, info, and warn
max_error = error_counter.most_common(1)
max_info = info_counter.most_common(1)
max_warn = warn_counter.most_common(1)

# Print the results
print("Most common ERROR:")
if max_error:
    print(f"Type: {max_error[0][0]}, Count: {max_error[0][1]}")
else:
    print("No errors found")

print("\nMost common INFO:")
if max_info:
    print(f"Type: {max_info[0][0]}, Count: {max_info[0][1]}")
else:
    print("No info messages found")

print("\nMost common WARN:")
if max_warn:
    print(f"Type: {max_warn[0][0]}, Count: {max_warn[0][1]}")
else:
    print("No warnings found")
