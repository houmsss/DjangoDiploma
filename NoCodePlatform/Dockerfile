FROM python:3.10

RUN mkdir /main
WORKDIR /main
RUN pip install --upgrade pip
COPY requirements.txt /main/

RUN pip install -r requirements.txt
COPY . /main/



