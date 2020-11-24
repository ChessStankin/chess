FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /chess
COPY requirements.txt /chess
RUN python3.9 -m pip install -r requirements.txt
COPY . /chess