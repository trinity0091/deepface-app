worker: python preload.py
web: uvicorn  run_app:app --host "0.0.0.0" --port $PORT --reload --ws 'auto' --loop 'auto' --workers 8