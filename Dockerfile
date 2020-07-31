FROM python:3.7.6
WORKDIR /app
COPY . .


ENV sqlUrl 172.17.0.1
#修改频道
RUN pwd
RUN pip -V
RUN pip install --upgrade pip
#安装到虚拟机的全局 不用激活
RUN pip install  -r requirements.txt
RUN pip install flasgger

RUN pip list
RUN echo "依赖安装完成==============="
EXPOSE 8389
# CMD：运行gunicorn
CMD ["gunicorn", "manage:app", "-c", "./gunicorn.conf.py","-preload" ]