FROM python:3.12-slim

# Install system dependencies for pyodbc and the SQL Server ODBC Driver
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    gnupg \
    gcc \
    g++ \
    unixodbc \
    unixodbc-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install the Microsoft ODBC Driver for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

EXPOSE 5000

# Set environment variables
ENV SQL_SERVER=${SQL_SERVER}
ENV SQL_DATABASE=${SQL_DATABASE}
ENV SQL_USERNAME=${SQL_USERNAME}
ENV SQL_PASSWORD=${SQL_PASSWORD}

# Command to run the application
CMD ["python", "-m", "app"]

