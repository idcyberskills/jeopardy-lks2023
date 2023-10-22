FROM python:3

RUN apt-get update 
RUN apt-get install -y socat 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*

RUN useradd -U -m -s /bin/bash adamaspcap

WORKDIR /home/adamaspcap

COPY ./chall.py .
COPY ./run.py .
COPY ./flag.txt .

RUN chown -R root:adamaspcap /home/adamaspcap
RUN chmod -R 750 /home/adamaspcap

CMD $
CMD [ "python", "./run.py" ]
