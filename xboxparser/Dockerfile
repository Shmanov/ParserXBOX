FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /xboxparser
COPY requirements.txt /xboxparser/
RUN pip install -r requirements.txt
COPY . /xboxparser/