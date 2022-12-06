#Docker image will be built using github actions
FROM ubuntu:20.04

ENV TIMEZONE America/Mexico_City
ENV JUPYTERLAB_VERSION 3.2.4
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV DEB_BUILD_DEPS="python3-dev python3-pip python3-setuptools software-properties-common"
ENV DEB_PACKAGES="sudo nano less git nodejs curl wget htop"

RUN apt update && export $DEBIAN_FRONTEND && \
    echo $TIMEZONE > /etc/timezone && apt install -y tzdata

RUN apt update && apt install -y $DEB_BUILD_DEPS $DEB_PACKAGES && \
    pip3 install --upgrade pip
    
RUN pip3 install jupyter jupyterlab==$JUPYTERLAB_VERSION --upgrade    

RUN jupyter notebook --generate-config && \
    sed -i "s/# c.NotebookApp.password = .*/c.NotebookApp.password = u'sha1:115e429a919f:21911277af52f3e7a8b59380804140d9ef3e2380'/" ~/.jupyter/jupyter_notebook_config.py
#effectively load password and configs
RUN cp ~/.jupyter/jupyter_notebook_config.py ~/.jupyter/jupyter_server_config.py
#install exiftool

RUN git clone https://github.com/exiftool/exiftool.git && cd exiftool && perl Makefile.PL && make && make test && make install

#install simex pkg
#next line works when building using github actions, assumes sipecam-metadata-extractor repo is cloned
COPY . /root/sipecam-metadata-extractor
RUN cd /root/sipecam-metadata-extractor/src && pip3 install .

VOLUME ["/shared_volume"]

