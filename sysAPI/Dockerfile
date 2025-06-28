FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install fastapi uvicorn fastapi[standard]

CMD ["fastapi", "run", "sysAPI.py"]
