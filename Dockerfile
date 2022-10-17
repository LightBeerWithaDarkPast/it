FROM compdatasci/spyder-desktop
MAINTAINER Grinenko Aleksandr 'Grinenko-aleksandr@mail.ru'
WORKDIR /app
COPY . .
CMD ['DZ1.py']
