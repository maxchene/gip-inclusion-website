FROM python:3.10

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV GECKODRIVER_URL=https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux32.tar.gz

# For behave tests
RUN apt-get update && apt-get install -y --no-install-recommends firefox-esr
RUN wget -qO- $GECKODRIVER_URL | tar xvz -C /usr/bin/

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
