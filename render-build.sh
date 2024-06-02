#!/usr/bin/env bash

# Install system dependencies
apt-get update
apt-get install -y libpq-dev libssl-dev

# Proceed with the usual pip install
pip install -r requirements.txt
