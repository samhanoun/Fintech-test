FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV DATABASE_URL=sqlite:///./transactions.db

EXPOSE 5000

# Run the app directly to avoid CLI import resolution issues
CMD ["python", "app.py"]
