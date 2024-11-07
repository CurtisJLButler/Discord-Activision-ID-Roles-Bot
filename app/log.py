# Example usage
# log_message(f"This is a log entry.")
# log.log_message(f"This is a log entry.")

# Get logs from a specific time range (default: last 10 days)
# logs = get_logs(0, 0)  # Get logs from the last 10 days


import json
import datetime
import os

def log_message(message):
    
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "message": message
    }
    print(f"[{log_entry['timestamp']}]  {log_entry['message']}")

    # Check if the file exists and is not empty
    if os.path.exists('log.json'):
        with open('log.json', 'r+') as file:
            try:
                # Try to load existing JSON data
                data = json.load(file)
            except json.JSONDecodeError:
                # If the file is empty or corrupted, start with an empty list
                data = []

            # Add the new log entry
            data.append(log_entry)

            # Move the file pointer to the beginning
            file.seek(0)
            # Write the updated list back to the file
            json.dump(data, file, indent=4)
    else:
        # If the file doesn't exist, create it with an array containing the first log entry
        with open('log.json', 'w') as file:
            json.dump([log_entry], file, indent=4)

def get_logs(start_time_str, end_time_str):
    # Convert string times to datetime objects
    if start_time_str == 0:
        start_time = datetime.datetime.now() - datetime.timedelta(days=10)
    else:
        start_time = datetime.datetime.fromisoformat(start_time_str)

    if end_time_str == 0:
        end_time = datetime.datetime.now()
    else:
        end_time = datetime.datetime.fromisoformat(end_time_str)
    
    print(f"Fetching logs from {start_time} to {end_time}")  # Debugging print

    logs_in_range = []

    # Check if the log file exists
    if os.path.exists('log.json'):
        with open('log.json', 'r') as file:
            try:
                # Load the existing log data
                data = json.load(file)
            except json.JSONDecodeError:
                # If the file is empty or corrupted, return an empty list
                return []

            # Filter logs based on the time range
            for log in data:
                log_time = datetime.datetime.fromisoformat(log["timestamp"])
                if start_time <= log_time <= end_time:
                    # Append only the string values (timestamp and message)
                    logs_in_range.append(f"[{log['timestamp']}]  {log['message']}")
    for log in logs_in_range:
        print(log)
    return logs_in_range




