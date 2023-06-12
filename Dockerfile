FROM python:3.10

WORKDIR /sample_api

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]