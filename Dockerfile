FROM python:3.7.8
WORKDIR /app
COPY . .
#修改频道
RUN pip -V
RUN pip3 -V
RUN ls
#RUN pip install --upgrade pip
RUN pip install  -r requirements.txt
RUN pip list
RUN echo "依赖安装完成==============="
EXPOSE 8389
# CMD：运行gunicorn
CMD ["gunicorn", "manage:app", "-c", "./gunicorn.conf.py","-preload" ]