import re
from collections import Counter

# Assigning a variable called log_pattern to the regex expression to find the user and ip address from failed login
log_pattern = re.compile(r"Failed password for (invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+) port")

# Function to analyse log files with the regex expression previously assigned
def analyse_logs(log_file):
    failed_attempts = []

    # Opens log file with specific encoding rules and ignores errors
    with open (log_file, "r", encoding="utf-8", errors="ignore") as file:
        # Goes through log line by line to see if there is a match between the contents of the file and the regex expression
        for line in file:
            match = log_pattern.search(line)
            if match:
                username = match.group(2)
                ip_address = match.group(3)
                failed_attempts.append((ip_address, username))
    
    # Extracts ip addresses from failed_attempts and counts each unique ip address
    ip_counts = Counter(ip for ip, user in failed_attempts)

    # Prints 5 most frequent ip addresses along with respective count
    print("\n Failed SSH Login Attempts:")
    for ip, count in ip_counts.most_common(5):
        print(f" {ip} - {count} failed attempts")
        # if failed attempts is greater than 5 flags as possible brute force attempt
        if count > 5:
            print (f" Possible brute force attack detected from {ip}!")
if __name__ == "__main__":
    log_file = "C:/Users/frank/Desktop/Sample-logfile.log"
    analyse_logs(log_file)
