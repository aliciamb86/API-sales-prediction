FROM python:3.9-slim
RUN mkdir /src
WORKDIR /src
ADD . /src
RUN pip install -r requirements.txt
CMD ["python", "app_model_FastAPI.py"]
EXPOSE 8000
