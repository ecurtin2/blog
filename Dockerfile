FROM continuumio/miniconda3:4.6.14

# Download hugo
ENV HUGO_VERSION=0.55.6
RUN wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz

# Extract
RUN python -m tarfile -e hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz /hugo
RUN rm hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz

# Move to path and delete extras
RUN mv /hugo/hugo /usr/bin/hugo
RUN rm -rf /hugo

# Install python stuff
COPY requirements.txt /requirements.txt
RUN conda install --file requirements.txt

WORKDIR /mnt

# Hugo server is port 1313 by default
EXPOSE 1313