FROM python:3.14-slim
WORKDIR /projects
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -m userapp
USER userapp
CMD ["sleep", "infinity"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]