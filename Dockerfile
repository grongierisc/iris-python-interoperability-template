ARG IMAGE=intersystemsdc/iris-community:latest
FROM $IMAGE as builder

# use the root user to install packages
USER root   

# create a directory for the application     
WORKDIR /irisdev/app
RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /irisdev/app
USER ${ISC_PACKAGE_MGRUSER}

# Copy the source code
COPY . .
COPY iris.script /tmp/iris.script

# install required packages
RUN pip3 install -r requirements.txt

# environment variables for embedded python
ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD "SYS"
ENV IRISNAMESPACE "IRISAPP"

# create the namespace and install the application
RUN iris start IRIS \
	&& iris session IRIS < /tmp/iris.script \
    && /usr/irissys/bin/irispython -m grongier.pex -M /irisdev/app/src/python/reddit/settings.py \
    && iris stop IRIS quietly

FROM $IMAGE as final

ADD --chown=${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} https://github.com/grongierisc/iris-docker-multi-stage-script/releases/latest/download/copy-data.py /irisdev/app/copy-data.py

RUN --mount=type=bind,source=/,target=/builder/root,from=builder \
	cp -f /builder/root/usr/irissys/iris.cpf /usr/irissys/iris.cpf && \
	python3 /irisdev/app/copy-data.py -c /usr/irissys/iris.cpf -d /builder/root/ 

# environment variables for embedded python
ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD "SYS"
ENV IRISNAMESPACE "IRISAPP"

RUN pip install iris-pex-embedded-python

ENV LD_LIBRARY_PATH=${ISC_PACKAGE_INSTALLDIR}/bin:${LD_LIBRARY_PATH}

COPY --chown=${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} entrypoint.sh /

ENTRYPOINT [ "/tini", "--", "/entrypoint.sh" ]