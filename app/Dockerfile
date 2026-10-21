FROM python:3.9-slim
WORKDIR /app
RUN useradd -m appuser
USER appuser
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python',"app.py"]

