FROM python
WORKDIR /app
COPY ./app/* /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "simple_webapp.py"]

