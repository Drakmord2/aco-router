
# Python3
FROM python:3

# Dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Setup Matplotlib
COPY ./devops/matplotlibrc /root/.config/matplotlib/matplotlibrc

# Environment
ENV APP_ROOT="/var/www"

# Set the application root
WORKDIR ${APP_ROOT}

# Listen to port
EXPOSE 6000

# Setup application
COPY ./devops/start.sh /opt/start.sh
RUN chmod 755 /opt/start.sh

# Start application
ENTRYPOINT [ "/opt/start.sh" ]
