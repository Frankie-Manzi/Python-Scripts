import re
from collections import Counter, defaultdict

# Assigning a variable called log_pattern to the regex expression to find the user and ip address from failed login
user_pattern = re.compile(r"login attempt (invalid user )?(\S+/\S+) failed")
ip_pattern = re.compile(r'\b((?:\d{1,3}\.){3}\d{1,3})\b')

# Function to analyse log files with the regex expression previously assigned
def analyse_logs(log_file):
    failed_attempts = []
    usernames_per_ip = defaultdict(set)

    # Opens log file with specific encoding rules and ignores errors
    with open (log_file, "r", encoding="utf-8", errors="ignore") as file:
        # Goes through log line by line to see if there is a match between the contents of the file and the regex expression
        for line in file:
            user_match = user_pattern.search(line)
            ip_match = ip_pattern.search(line)
            if user_match and ip_match:
                username = user_match.group(2)            
                ip_address = ip_match.group(0)
                failed_attempts.append((ip_address, username))
                usernames_per_ip[ip_address].add(username)
    # Extracts ip addresses from failed_attempts and counts each unique ip address
    ip_counts = Counter(ip for ip, user in failed_attempts)

    # Prints 5 most frequent ip addresses along with respective count
    print("\n Failed Login Attempts:")
    for ip, count in ip_counts.most_common(5):
        print(f" {ip} - {count} failed attempts")
        # if failed attempts is greater than 5 flags as possible brute force attempt
        if count > 5:
            print (f" Possible brute force attack detected from {ip}!")
            # Count usernames used per specific IP
            username_list = list(usernames_per_ip[ip])
            username_counts = Counter(username_list)
            most_common_usernames = username_counts.most_common(5)

            # Format and display the top 5 most common usernames
            formatted_usernames = ', '.join(f"[{u}]" for u, _ in most_common_usernames)
            print(f" Usernames attempted: {formatted_usernames}", end='')

            # If there are more than 5 usernames attempted, print the remaining value of usernames attempted
            if len(username_list) > 5:
                remaining = len(username_list) - 5
                print(f", and {remaining} other usernames used.")
            else:
                print()
    return failed_attempts
if __name__ == "__main__":
    log_file = "C:/Users/frank/Downloads/HoneyPot-Logs.JSON"
    analyse_logs(log_file)
