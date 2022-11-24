#!/bin/sh

echo Starting application server
poetry run flask --app news-tracker run --host 0.0.0.0
