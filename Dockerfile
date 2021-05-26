# Base image
FROM python:3.7

# Run Dependencies
COPY requirements.txt /
RUN pip install -r requirements.txt

# Copy files
COPY forecaster.py /
COPY app.py /

EXPOSE 8080

CMD ["python", "app.py"]
