# ThreaThor

by aseng

---

## Flag

```
LKS{we_f!n4LLy_PWNED_Adamas_tr4ffic_filled_with_m4lware_varietie5}
```

## Description
Our company, PT LKSN Tbk., has suffered a dangerous breach of an APT malware from Bali called **Adamas**.
The malware itself has a lot of capabilities including **turning off our defense perimeters software**. The last thing that 
the DFIR team did, fortunately, was turning on the Wireshark toolings for a D2D jobdesk as well and they have captured a pretty
interesting artifacts in the traffic.

Can you, as a future `threat intelligence` candidate, help us? You are permitted to **ANSWER** all the questions related to the malware.

Download the PCAP Traffic & Questions File [here](https://drive.google.com/drive/folders/1t1eQgTnOYVvPovAmj4nl_eUDssOfXVqu?usp=sharing)

Connect with netcat to answer the questions and get your FLAG remotely from here:

`nc hostname 27545`

## Difficulty
easy/medium

## Hints
> Intentionally left empty

## Tags
pcap, malwares

## Deployment
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run using `run.sh` script in `src/` folder