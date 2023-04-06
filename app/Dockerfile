FROM python:alpine

EXPOSE 5000

WORKDIR /app

# Install all the requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy all the flask project files into the WORKDIR
COPY . .

# Execute flask application inside the container
CMD python3 app.py