FROM python: 3.11.6
WORKDIR /app
COPY requirements.txt ./
Run pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "test_main.py"]
EXPOSE 8000
