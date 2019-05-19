FROM continuumio/miniconda3:4.6.14

RUN wget https://github.com/gohugoio/hugo/releases/download/v0.55.6/hugo_extended_0.55.6_Linux-64bit.tar.gz
COPY requirements.txt /requirements.txt
RUN conda install --file requirements.txt
RUN python -m tarfile -e hugo_extended_0.55.6_Linux-64bit.tar.gz /hugo
RUN rm hugo_extended_0.55.6_Linux-64bit.tar.gz
RUN mv /hugo/hugo /usr/bin/hugo
RUN rm -rf /hugo
WORKDIR /mnt