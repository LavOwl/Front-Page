FROM python:3.12-slim 
#slim for reduced size, latest stable version as of 2025. Runs over basic Docker OS

ENV PYTHONDONTWRITEBYTECODE 1
#Creates clutter pyc files that don't much help for a project of this scale
ENV PYTHONUNBUFFERED 1
#Disabled buffering for real-time updated and full-logs in case of a crash. Otherwise Docker handles logs in chunks.

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    zlib1g-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY dependencies.txt .

RUN pip install --upgrade pip && pip install -r dependencies.txt

COPY . .

CMD ["python", "entrypoint.py"]