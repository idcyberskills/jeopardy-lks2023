flag1 = False
flag2 = False
flag3 = False
flag4 = False

print("""
In all installed agents, how many times successful authentication happens and how many times failed login attempts? (concat sucessful and failed with underscores RESPECTIVELY)
Example: 5 failed, 2 success then answer is 2_5
    """)
answer1 = input(">>: ")
if answer1 == "58_250" or answer1 =="56_250":
    print('Correct!\n')
    flag1 = True
else:
    print('Wrong!\n')


print("""
There has been a login to a non-existent user in the default agent server via SSH. When does this happening for the first time? How many times does it occur?

Answer in a format of YYYY-MM-DD HH:MM:SS.MSS_X

If you think that it happens on 14/09/2022 13:02:15/012 and it occurs 100000 times, then the answer is : 2022-09-14 13:02:15.012_100000
    """)
answer2 = input(">>: ")
if answer2 == "2023-10-07 19:22:07.021_10":
    print('Correct!\n')
    flag2 = True
else:
    print('Wrong!\n')


print("""
3. There has been an account deletion in one of the installed agents located in Windows Server. What's the account name & its SID which is deleted? Since this activity also triggers a Windows Event, what's the event ID number?

Format answer: accountname_sidnumber_eventidnumber

Example: rudolph_S-1-5-18919109109_2176
    """)
answer3 = input(">>: ")
if answer3 == "aseng_S-1-5-21-3293318168-2717711385-4291385379-1006_4726":
    print('Correct!\n')
    flag3 = True
else:
    print('Wrong!\n')


print("""
4. According to CIS Microsoft Windows 10 Enterprise Benchmark v1.12.0 policy listed, it looks like Kerberos Encryption Type is still insecure. What's the name of registry key that checks this type?

Answer format excludes the HIVE , for example if the registry full path key is HKLM\\Software\\Paramont\\Enckeytype then the answer is Enckeytype.
Note that this answer is also case sensitive so you need to pay attention on the capital letter.
    """)
answer4 = input(">>: ")
if answer4 == "SupportedEncryptionTypes":
    print('Correct!\n')
    flag4 = True
else:
    print('Wrong!\n')



if flag1 and flag2 and flag3 and flag4:
    print("I hope you didn't brute force the question >:u , anyway you're so good! Here's your flag:")
    print("LKS{y0u_4r3_th3_next_gen_S0C_4nal!st_wazzzzzzuhhhhhhhhhh}")
else:
    print('If you get this message but you got all answers correct, please contact aseng and send the proof + each of your answers.')
