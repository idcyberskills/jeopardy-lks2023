# Adamas Revenge

by aseng

---

## Flag

```
LKS{y0u_just_4n4lyzed_an_APT_infection_m4lw4re!_wowww}
```

## Description
Previously, Adamas Malware breached our company internals but we've successfully recovered from that because
of your doing. Yet this week has been another blast since its variety come mimicking a valid software.

One of our employee is getting phished by someone to download it and executes a malicious batch script that 
infects the computer.

We're calling you again to end this madness of Adamas, and you'll cooperate with our DF Consultant to answer
each questions to perform a RCA. Note that the employee's computer has been deepfrozen and you'll be given
a Windows Image File.

Download the `.raw` file [here](https://drive.google.com/drive/folders/18TCKxvpuqIcOjAnmPcSpKBKu6j7Dj7vU?usp=sharing)

Zip Password: `LKS_4d4ma$_ch4LL3n9e!?#`

Connect with netcat to answer the questions and get your FLAG remotely from here:

`nc hostname 27544`

## Difficulty
medium

## Hints
> Intentionally left empty

## Tags
memory-forensic, APT, malwares

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run using `run.sh` script in `src/` folder