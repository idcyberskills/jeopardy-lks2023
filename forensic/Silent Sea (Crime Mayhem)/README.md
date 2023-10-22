# Silent Sea (Crime Mayhem)

by aseng

---

## Flag

```
LKS{y0u_4r3_th3_next_gen_S0C_4nal!st_wazzzzzzuhhhhhhhhhh}
```

## Description
After those Wazuh tutorials, you realize that there has been a malicious activity there. The SOC lead wants your report to be finished this evening and you supposed to answer all the questions related to the incident.

Tutorial on Importing the OVA in VMWare Player/Workstation can be viewed [here](https://nshielddocs.entrust.com/monitor/2.9.8/install-vmware-workstation)

Download the Wazuh OVA file [here](https://binusianorg-my.sharepoint.com/personal/felix_alexander_binus_ac_id/_layouts/15/guestaccess.aspx?share=EtsEXQcnzW9Jhe7Tv4bwVosBMRI2PbWs3EIOHcshcRSYWg&e=tat5uC)

All credentials related to the OVA and Wazuh:

```
Zip Password (Silent Sea.zip) = LK$2023_w4zUh_m4dn3zzz_mads!~~

Ubuntu Credentials (Login after boot OVA) =  silentsea:silentsea

Wazuh Admin Credentials = admin:6ebY4rgIUXmuCM2lH+8zhGwX7mUcavXp
```

**Notes: Wait for 5-10 minutes after OVA is booted (powered on) and you logged in as `silentsea:silentsea` credentials, and then visit https://127.0.0.1 in your main host, or if localhost is not working, get the ip address of the OVA by running command `ip -a` or `ifconfig` to get the `ens33`/`eth0`/`enp0s3` NIC IP Address IPv4**

If those steps are properly executed, you should be able to see Wazuh Dashboard Interface in your local machine. If it is still not, please immediately call the judges.

Connect to the `nc` and answer all of the questions.

`nc hostname 27542`

## Difficulty
easy

## Hints
> Intentionally left empty

## Tags
siem, wazuh

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run using `run.sh` script in `src/` folder