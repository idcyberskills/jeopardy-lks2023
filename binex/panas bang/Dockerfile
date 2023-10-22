FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update 
RUN apt-get install -y xinetd 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*

RUN useradd -U -m -s /bin/bash warm

WORKDIR /home/warm

COPY ./flag.txt .
COPY ./chall .
COPY ./run.sh ./run
COPY ./xinetd /etc/xinetd.d/xinetd
COPY ./startchall.sh /usr/bin/startchall

RUN chown -R root:warm /home/warm
RUN chmod -R 750 /home/warm && chmod 440 flag.txt 
RUN mv flag.txt flag-$(md5sum flag.txt | awk '{print $1}').txt
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall

EXPOSE 11101

CMD ["/usr/bin/startchall"]
