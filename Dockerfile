FROM python:3.10
RUN pip3 install fastapi uvicorn
COPY ./app /app
EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15400" ]