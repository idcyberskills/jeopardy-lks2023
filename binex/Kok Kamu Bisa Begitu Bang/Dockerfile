FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update 
RUN apt-get install -y xinetd 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*

RUN useradd -U -m -s /bin/bash canary

WORKDIR /home/canary

COPY ./flag.txt .
COPY ./chall .
COPY ./run.sh ./run
COPY ./xinetd /etc/xinetd.d/xinetd
COPY ./startchall.sh /usr/bin/startchall
COPY ./libc.so.6 .
COPY ./ld-linux-x86-64.so.2 .

RUN chown -R root:canary /home/canary
RUN chmod -R 750 /home/canary && chmod 440 flag.txt 
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall

EXPOSE 11102

CMD ["/usr/bin/startchall"]
