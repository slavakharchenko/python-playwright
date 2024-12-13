FROM python:3.12-bookworm

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers and dependencies
RUN playwright install chromium
RUN playwright install-deps

# Copy the project files into the container
COPY . .

# Define a build-time argument
ARG TEST_ID=all

# Set TEST_ID as an environment variable
ENV TEST_ID=${TEST_ID}

# Command to run tests
ENTRYPOINT ["bash", "run_tests.sh"]
# CMD ["pytest"]