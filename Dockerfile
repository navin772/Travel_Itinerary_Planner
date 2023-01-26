FROM python:3.10-slim
COPY . /app
WORKDIR /app
EXPOSE 8000
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD [ "main.py" ]