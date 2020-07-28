FROM continuumio/miniconda3
MAINTAINER flask <3093265766@qq.com>

WORKDIR /app
COPY . .
#修改频道
RUN pip -V

RUN pip install -r requirements.txt
#RUN conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
#RUN conda config --add channels http://mirrors.ustc.edu.cn/anaconda/pkgs/main
#RUN conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
##查看频道
#RUN conda config --get channels
#RUN conda env create -f environment.yaml
#
#SHELL ["conda","run","-n","flask","/bin/bash","-c"]


# RUN wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
# RUN bash ~/miniconda.sh -b -p /miniconda
#

RUN echo "依赖安装完成==============="

# CMD：运行gunicorn
CMD ["gunicorn", "manage:app", "-c", "./gunicorn.conf.py"]