# Linux Commands Guide (Ubuntu/Kali)
For more understanding, try it yourself.

## Installing WSL
```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```
After restart:
```
wsl --install
```
After restart, go to Microsoft Store, pick whatever distribution you like & install it.

## Working Directory (WD)
- To check the working directory use `pwd`
#### `cd` (Change Directory)
Usage: `cd {PATH}`
- To get to parent folder use `cd ..`
- To get to grandparent folder use `cd ../..`
- To get to root `cd /`
- To get to home `cd ~`
- To get to a child directory `cd ./child/childofchild`

## Root Permissions
- Append `sudo` before any command to run as root
- To login as root use `sudo su -`

## Files/Directories
- Creating file: `touch file.txt`
- Creating directory: `mkdir dir`
- Moving file: `mv file.txt /path/to/anothername.txt`
- Renaming file: `mv file.txt another.txt`
- Removing file: `rm file.txt`
- Removing Directory: `rm -d`
- Listing all contents of WD: `ls`
- Listing all contents of WD with extra details: `ll`
- Copying a file: `cp old_code.cpp new_code.cpp`

## Working with files
- To output the file `cat file.txt`
- To edit the file `sudo nano file.txt`

## Running executables
- Running a local executable `./app`
- Running a global executable `app`
- Running a global executable that matchs some command `\app`

## Package Manager
- Installing: `sudo apt install {package}`
- Updating: `sudo apt update`
- Upgrading `sudo apt upgrade`
- Removing `sudo apt remove {package}`

## Helping Programs
- `timeout {SECONDS} {COMMAND}` - Exits with error code 127 in case it exceeds time
- `time {COMMAND}` - Measures execution time of a command
- `cron` - Schedule programs & scripts, for using `crontab -e`
- `curl` - Client for sending web requests
- `man {PROGRAM_NAME}` - Tells you how to use the program/command
- `which {PROGRAM_NAME}` - Shows you the path of the program

## Environment Variables
The system has some variables with assigned values, so programs can use it
- Checking environment variables: `env`
- Writing an environment variable in current session: `export VAR="value"`
- Writing a permanent environment variable: `echo 'export VAR="value"' >> ~/.bashrc`
- Outputting an environment variable: `echo $VAR`
- Outputting last exit code: `echo $?`

## File Permissions
When doing `ll`, here is an expected output:
```
drwxrwxrwx root root
lrwxr-xr-- root root
-rw-rw-r-- user user
```
- First character: file type d=directory, l=link, -=file
- Next 3 characters: Permissions of owner
- Next 3 characters: Permissions of group
- Next 3 characters: Permissions of others
- Permissions `rwx` means **r**ead, **w**rite, e**x**ecute.
- After it the owner
- After it the group

- Changing owner: `chown`
- Changing group: `chgrp`
- Changing permissions: `chmod`

For more, check [this page](https://help.ubuntu.com/community/FilePermissions)
## Tricks
- You can do multiple commands in same line:
  - `mkdir child; cd child` - Using `;` it will run these two commands
  - `mkdir child && cd child`- Using `&&` it will run the second command if the first have a zero exit code
  - `./code | ./checker` - Using `|` it will run first command and redirect its output to second command input
