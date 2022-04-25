#FROM python:3.8.0
#EXPOSE 8501
#WORKDIR /app
#COPY requirements.txt ./requirements.txt
#RUN pip3 install -r requirements.txt
#COPY . .
#ENTRYPOINT ["streamlit", "run"] 
#CMD ["test.py"]

FROM python:3.8.0
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
ADD test.py .
#ENTRYPOINT ["python"]
CMD ["streamlit" , "run", "test.py"]