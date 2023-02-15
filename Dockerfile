FROM python:alpine

COPY 'src/' '/home/'

RUN mkdir -p /home/output/

WORKDIR '/home'

CMD [ "/home/entry_script.sh" ]