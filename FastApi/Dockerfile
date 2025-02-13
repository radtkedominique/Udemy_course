#textbeschreibung für image
FROM python:latest
#LABEL authors="dominique.radtke"

#ENTRYPOINT ["top", "-b"]


WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV PORT=8000
CMD ["sh", "-c", "uvicorn fastapi_upload:app --host 0.0.0.0 --port 8000"]
