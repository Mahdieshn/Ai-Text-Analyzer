# 1. Base Image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Download NLP Model (Important!)
RUN python -m spacy download en_core_web_sm

# 5. Copy project files
COPY . .

# 6. Expose port and run
EXPOSE 8000
CMD ["python", "main.py"]