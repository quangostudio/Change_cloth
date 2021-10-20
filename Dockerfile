FROM python:3.6

WORKDIR /app

COPY . .
ENV PORT 5555

RUN pip install -r requirements.txt

CMD ["python", "run.py"]