FROM python:3-alpine

# Create app directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install app dependencies
RUN pip install --upgrade pip
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000
#CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000"]
CMD [ "waitress-serve", "--host", "127.0.0.1", "app:app"]