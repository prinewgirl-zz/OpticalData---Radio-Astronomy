FROM williamyeh/python2

WORKDIR /

RUN pip install pip --upgrade \
    && pip install numpy --no-cache-dir \
    && pip install healpy --no-cache-dir \ 
    && pip install six --upgrade \
    && pip install astroquery --no-cache-dir \
    && pip install wheel --no-cache-dir \
    && pip install pandas --no-cache-dir \
    && pip install astropy --no-cache-dir

RUN apt update && apt install git -y \
    && git clone http://github.com/rlwastro/mastcasjobs.git \ 
    && git clone https://github.com/marinscosmo/PS1zxcorr.git \
    && pip install git+git://github.com/dfm/casjobs@master

WORKDIR /mastcasjobs

RUN git checkout 3c27f7ff7aff933694058b5204abd72527115244 \
    && pip install -e /mastcasjobs  
 

WORKDIR /
 
RUN apt remove git -y \
    && pip uninstall pip  -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* 

COPY run.sh /run.sh

RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
CMD [ "python", "/PS1zxcorr/run_PS1zxcorr.py" ]
