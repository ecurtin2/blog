FROM continuumio/miniconda3:4.6.14-alpine

RUN wget https://github.com/gohugoio/hugo/releases/download/v0.55.6/hugo_extended_0.55.6_Linux-64bit.tar.gz -P .

