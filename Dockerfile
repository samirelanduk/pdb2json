FROM continuumio/anaconda3

RUN mkdir -p /home/app

WORKDIR /home/app

COPY ./ ./

RUN sed -i s/'DEBUG = True'/'DEBUG = False'/g pdb2json.py

RUN sed -i s/'ALLOWED_HOSTS = \[\]'/'ALLOWED_HOSTS = \["*"]'/g pdb2json.py

RUN conda install numpy

RUN conda install scipy

RUN pip install gunicorn

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "--bind", ":80", "--workers", "3", "pdb2json:application"]