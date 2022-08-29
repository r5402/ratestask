FROM python:slim

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

COPY app.py .
CMD ["flask", "run"]
