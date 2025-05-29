#!/bin/bash

# Ejecuta Gunicorn con el worker adecuado para ASGI
gunicorn main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
