#!/bin/sh
set -e

# Load the .env file into environment variables
export $(grep -v '^#' .env | xargs)

# Generate the final ngrok.yml file
envsubst < ngrok/ngrok.yml.template > ngrok/ngrok.yml

# Start Docker
docker compose up --build