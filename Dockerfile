FROM python:3.10-alpine

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY ./src /bys
WORKDIR /bys
EXPOSE 80

ENTRYPOINT ["gunicorn", "-w","2", "--threads", "2", "-b", "0.0.0.0:80", "wsgi:app"]