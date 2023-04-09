# Lightweight Python
FROM python:3.10-slim

# Allow Statements and Log Messages to Immediately Appear in the Knative Logs
ENV PYTHONUNBUFFERED True

# Copy Local Code to the Container Image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install Production Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Web Service
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app