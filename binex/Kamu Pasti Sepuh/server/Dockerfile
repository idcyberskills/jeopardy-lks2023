FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update 
RUN apt-get install -y xinetd 
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*

RUN useradd -U -m -s /bin/bash heap

WORKDIR /home/heap

COPY ./flag.txt .
COPY ./chall .
COPY ./run.sh ./run
COPY ./xinetd /etc/xinetd.d/xinetd
COPY ./startchall.sh /usr/bin/startchall

RUN chown -R root:heap /home/heap
RUN chmod -R 750 /home/heap && chmod 440 flag.txt 
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall

EXPOSE 11103

CMD ["/usr/bin/startchall"]
