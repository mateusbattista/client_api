FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir cliente_api
WORKDIR /cliente_api
ADD . /cliente_api
RUN pip install -r requirements.txt
