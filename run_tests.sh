#!/bin/bash

# Check if TEST_ID is not set
if [ -z "$TEST_ID" ]; then
    echo "TEST_ID not set. Defaulting to 'all'."
    export TEST_ID=all
fi

echo "Running tests with TEST_ID: $TEST_ID"

# Run pytest with the environment variable
if [ "$TEST_ID" = "all" ]; then
    pytest
else
    pytest -m "test_id_$TEST_ID"
fi