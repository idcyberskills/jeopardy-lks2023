flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False

print("""
1. There's a LSASS Memory Dumping Attempt using one of the tools that is located in the user's Public folder. What's the name of that tool (including extension, for example: haha.exe)?
    """)
answer1 = input(">>: ")
if answer1 == "procdump64.exe":
    print('Correct!\n')
    flag1 = True
else:
    print('Wrong!\n')


print("""
2. Regarding to previous question, the dumped file is located in the temporary folder. What's the name of the dumped file (including extension, for example: password.raw)?
    """)
answer2 = input(">>: ")
if answer2 == "somethingwindows.dmp":
    print('Correct!\n')
    flag2 = True
else:
    print('Wrong!\n')


print("""
3. There's a "fake" Windows service installed from a non-existing user temporary folder. The service itself is an executable with ".exe" extension. What's the name of that executable (excluding the extension, for example if the name is yaya.exe, then the answer is yaya)?

    """)
answer3 = input(">>: ")
if answer3 == "0c134c70-2b4d-4cb3-beed-37c5fa0451d0":
    print('Correct!\n')
    flag3 = True
else:
    print('Wrong!\n')


print("""
4. There seems to be a shceduled task to be run. Although it's not running yet, How often does this task run in minutes and when's the scheduled date? Concatenate the answer with underscores! (_)
    
Example:  If you found that the task is running every hour and the scheduled date is 13-08-2023 08:20:32, then the answer is 60_13-08-2023_08:20:32

    """)
answer4 = input(">>: ")
if answer4 == "5_14-09-2023_13:00:00":
    print('Correct!\n')
    flag4 = True
else:
    print('Wrong!\n')

print("""
5. There's a persistence technique used from the malware. It executes a technique just like from the MITRE ATT&CK ID T1037.100. What's the full command which executes in a boot/logon initialization script?

For example, if the command is "powershell.exe -ep Bypass F:\\Capariya\\189209209309302020.ps1" then it's the answer (include all the symbols, digits and spaces)
    """)
answer5 = input(">>: ")
if answer5 == "C:\\TMP\\mim.exe sekurlsa::LogonPasswords > C:\\TMP\\o.txt":
    print('Correct!\n')
    flag5 = True
else:
    print('Wrong!\n')

if flag1 and flag2 and flag3 and flag4 and flag5:
    print("I hope you didn't brute force the question >:u , anyway you're so good! Here's your flag:")
    print("LKS{y0u_just_4n4lyzed_an_APT_infection_m4lw4re!_wowww}")
else:
    print('If you get this message but you got all answers correct, please contact aseng and send the proof + each of your answers.')