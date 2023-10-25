flag1 = False
flag2 = False
flag3 = False
flag4 = False

print("""
1. How many agents are available in the Wazuh Dashboard Server (including the default) ? What are their names? (concat with underscores)

Format: totalagent_agentnames

Example: 3_toba_semeru_jenengans
    """)
answer1 = input(">>: ")
if answer1 == "2_windah_silentsea" or answer1 == "2_silentsea_windah":
    print('Correct!\n')
    flag1 = True
else:
    print('Wrong!\n')


print("""
2. What's the hostname of the agent which has a Windows 10 Enterprise product?

Example: JUMINTEN-ABC123
    """)
answer2 = input(">>: ")
if answer2 == "DESKTOP-LCC9E2D":
    print('Correct!\n')
    flag2 = True
else:
    print('Wrong!\n')


print("""
3. In the last 1 year, when does the Wazuh logging started for the first time?

Answer in a format YYYY-MM-DD HH:MM:SS:MLS, for example 2021-08-17 14:32:21.169

    """)
answer3 = input(">>: ")
if answer3 == "2023-10-07 19:01:33.182":
    print('Correct!\n')
    flag3 = True
else:
    print('Wrong!\n')


print("""
4. How many TOTAL events related with MITRE ATT&CK from October 7th 2023 to October 8th 2023?
    """)
answer4 = input(">>: ")
if answer4 == "354" or answer4 == "356":
    print('Correct!\n')
    flag4 = True
else:
    print('Wrong!\n')

if flag1 and flag2 and flag3 and flag4:
    print("I hope you didn't brute force the question >:u , anyway you're so good! Here's your flag:")
    print("LKS{warming_uP_w1th_SIEM_is_real_life_forensic_challenge}")
else:
    print('If you get this message but you got all answers correct, please contact aseng and send the proof + each of your answers.')
