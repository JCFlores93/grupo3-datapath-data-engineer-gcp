FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./main.py /app/main.py
RUN mkdir csv
CMD ["python", "-u", "main.py"]