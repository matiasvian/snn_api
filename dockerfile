FROM --platform=arm64 python:3.8.5-slim-buster

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY app/data/pnr.txt data/pnr.txt
COPY app/SNN_api.py SNN_api.py
COPY app/SNN_logic.py SNN_logic.py
COPY app/SNN_tests.py SNN_tests.py

EXPOSE 8000

CMD ["uvicorn", "SNN_api:app", "--host=0.0.0.0", "--port=8000"]
