import platform

# Check the current OS
if platform.system() != "Darwin":
    # Stop the script here if the OS is not Mac OS
    exit()

# Ask how many applications the user has installed
num_apps = int(input("How many applications do you have installed? "))

# Ask for app directories for each app
app_directories = []
for i in range(num_apps):
    app_directory = input(f"Enter the directory for app {i+1}: ")
    app_directories.append(app_directory)

# Detect for a "~/.zshrc" file
zshrc_file = "~/.zshrc"

# For every directory
for directory in app_directories:
    # Append "function [app name without spaces) { [directory] $1; }" to the .zshrc file
    with open(zshrc_file, "a") as file:
        app_name = directory.replace(" ", "")
        file.write(f"function {app_name} {{ {directory} $1; }}\n")
