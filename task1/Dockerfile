FROM compdatasci/spyder-desktop
MAINTAINER Grinenko Aleksandr 'Grinenko-aleksandr@mail.ru'
WORKDIR /DZ1
COPY . .
RUN make /DZ1
RUN python spyder-desktop.py -p
CMD ['spyder-desktop.py', 'DZ1.py']
