FROM python:alpine

COPY 'src/' '/home/'
COPY 'data/' '/home/data'

RUN mkdir -p /home/output/

WORKDIR '/home'

CMD [ "/home/entry_script.sh" ]