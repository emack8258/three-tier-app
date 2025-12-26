# Use a lightweight Python image
FROM python:3.11-slim

# Set CPU-efficient environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install packages
# COPY VPN Bundle cert
COPY ./tmp/vpn_ca_bundle.pem /usr/local/share/ca-certificates/vpn_ca_bundle.crt

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping \
    curl \
    ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Add the certificate to the trust list
RUN chmod 644 /usr/local/share/ca-certificates/vpn_ca_bundle.crt \
    && update-ca-certificates

RUN update-ca-certificates --fresh
RUN ls -l /etc/ssl/certs 

# This tells Python where to find the combined certificate bundle.
ENV REQUESTS_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt"
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]