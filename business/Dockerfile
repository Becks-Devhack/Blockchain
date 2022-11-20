FROM blockchain_rest_api:latest
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 80
CMD ["python", "script.py"]