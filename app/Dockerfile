FROM python:3.9

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt && \
apt-get update && apt-get install -y iputils-ping netcat

# CMD python app_new.py
CMD ["uwsgi", "app.ini"]