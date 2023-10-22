FROM python:3

RUN apt-get update 
RUN apt-get install -y socat 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*

RUN useradd -U -m -s /bin/bash silentfeline

WORKDIR /home/silentfeline

COPY ./chall.py .
COPY ./run.py .
COPY ./flag.txt .

RUN chown -R root:silentfeline /home/silentfeline
RUN chmod -R 750 /home/silentfeline

CMD $
CMD [ "python", "./run.py" ]
