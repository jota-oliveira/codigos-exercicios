FROM debian

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils && \
	apt-get upgrade -y && \
	apt-get install -y apt-transport-https ca-certificates curl software-properties-common gpg apache2 apache2-utils wget && \
	wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add - && \
	echo "deb https://packages.sury.org/php/ stretch main" | tee /etc/apt/sources.list.d/php.list

RUN apt-get update && apt-get install -y php7.0 php7.0 libapache2-mod-php7.0 php7.0-mysql php-common php7.0-cli php7.0-common php7.0-json php7.0-opcache php7.0-readline

RUN echo "<Directory /var/www/>" >> /etc/sysctl.conf && \
	echo "Options Indexes FollowSymLinks" >> /etc/sysctl.conf && \
    echo "AllowOverride All" >> /etc/sysctl.conf && \
    echo "Require all granted" >> /etc/sysctl.conf && \
	echo "</Directory>" >> /etc/sysctl.conf && \
	rm /var/www/html/index.html && \
	a2enmod php7.0 && \
	sed -i -e 's/display_errors Off/display_errors On/g' /etc/php/7.0/apache2/php.ini && \
	sed -i -e 's/display_startup_errors Off/display_startup_errors On/g' /etc/php/7.0/apache2/php.ini && \
	sed -i -e 's/log_errors Off/log_errors On/g' /etc/php/7.0/apache2/php.ini && \
	sed -i -e 's/track_errors Off/track_errors On/g' /etc/php/7.0/apache2/php.ini  && \
	service apache2 start


VOLUME /var/www/html/projeto
WORKDIR /var/www/html
EXPOSE 80
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
