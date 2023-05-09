FROM python:latest

ADD SatSys.py .

CMD ["python", "./SatSys.py"]
