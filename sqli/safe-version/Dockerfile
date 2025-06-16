FROM python:3.9-slim

WORKDIR /app

COPY main.py /app/

RUN pip install flask

EXPOSE 5000

CMD ["python", "main.py"]
