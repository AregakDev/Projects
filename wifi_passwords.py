import subprocess

output = subprocess.check_output("netsh wlan show profile", shell=True)

# Decode the output from bytes to string
output = output.decode("utf-8")

# Split the output by line
profiles = output.split("\n")

# Extract profile names
profile_names = [p.split(":")[1][1:-1] for p in profiles if "All User Profile" in p]

# Get password for each profile
passwords = {}
for name in profile_names:
    try:
        # Get the output for the given profile
        profile_output = subprocess.check_output(f"netsh wlan show profile {name} key=clear", shell=True)
        
        # Decode the output from bytes to string
        profile_output = profile_output.decode("utf-8")
        
        # Split the output by line
        profile_lines = profile_output.split("\n")
        
        # Find the line containing the password
        for line in profile_lines:
            if "Key Content" in line:
                password = line.split(":")[1][1:-1]
                passwords[name] = password
                break
    except subprocess.CalledProcessError:
        passwords[name] = "PASSWORD NOT FOUND"

# Print the passwords
for name, password in passwords.items():
    print(f"{name}: {password}")
