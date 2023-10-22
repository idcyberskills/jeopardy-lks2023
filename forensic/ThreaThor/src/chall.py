flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
flag6 = False
flag7 = False
flag8 = False

print("""
1. When does the packet captures start? (Answer in format YYYY-MM-DD HH:MM:SS in GMT+7 timezone)

Example: 2023-01-12 01:12:35
  """)
answer1 = input(">>: ")
if answer1 == "2023-09-09 16:01:43":
    print('Correct!\n')
    flag1 = True
else:
    print('Wrong!\n')


print("""
2. What's the victim IP Address? (in IPv4 format)

Example: 13.37.73.371
   """)
answer2 = input(">>: ")
if answer2 == "192.168.239.128":
    print('Correct!\n')
    flag2 = True
else:
    print('Wrong!\n')


print("""
3. How many malicious domains do the user try to visit at the near of the packet captures before making a request to 23.277.199.27?
There's also a malicious domain that is hosted in a FREE web hosting app, what's the name of that domain?
(Answer Format NUMBERS_DOMAINNAME), example: 12_anjay.com

    """)
answer3 = input(">>: ")
if answer3 == "5_pate1k.000webhostapp.com":
    print('Correct!\n')
    flag3 = True
else:
    print('Wrong!\n')


print("""
4. There's an ongoing IRC traffic as well. What's the server connection password when the username 'user22f25' is prompted?

Example: password123

    """)
answer4 = input(">>: ")
if answer4 == "password22f2583b":
    print('Correct!\n')
    flag4 = True
else:
    print('Wrong!\n')

print("""
5. There's an upcoming OOB (Out-of-Bound) attack vector. Can you find the name of the last resolved domain ?   

Example: jajajajaj.baba.basreng.lks.com

	""")
answer5 = input(">>: ")
if answer5 == "gypkizkcmtrtuwaozxxxkyaehtjvdbozt.oast.site":
    print('Correct!\n')
    flag5 = True
else:
    print('Wrong!\n')


print("""
6. A cryptomining attempt exists as well in the traffic, pleace state the remote procedure call protocol version and also the stratum client notify ID response. Concat the answer with underscores!

Example, if you get the protocol version is 13.1 and the ID is a435-jajang, then the answer is 13.1_a435-jajang

	""")
answer6 = input(">>: ")
if answer6 == "2.0_2900501dcf6d9e31":
    print('Correct!\n')
    flag6 = True
else:
    print('Wrong!\n')

print("""
7. When does the SSH file transfer occurs? (Answer in format YYYY-MM-DD HH:MM:SS in GMT+7 timezone)

Example: 2023-01-12 01:12:35

	""")
answer7 = input(">>: ")
if answer7 == "2023-09-09 16:05:41":
    print('Correct!\n')
    flag7 = True
else:
    print('Wrong!\n')

print("""
8. Where's exactly the destination of the file transfer (Answer format: domain.name)

	""")
answer8 = input(">>: ")
if answer8 == "ssh.sandbox-services.alphasoc.xyz":
    print('Correct!\n')
    flag8 = True
else:
    print('Wrong!\n')

if flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8:
    print("I hope you didn't brute force the question >:u , anyway you're so good! Here's your flag:")
    print("LKS{we_f!n4LLy_PWNED_Adamas_tr4ffic_filled_with_m4lware_varietie5}")
else:
    print('If you get this message but you got all answers correct, please contact aseng and send the proof + each of your answers.')