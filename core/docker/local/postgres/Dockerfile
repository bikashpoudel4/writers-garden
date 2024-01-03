# FROM postgres:15-bullseye

# COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance

# RUN chmod +x /usr/local/bin/maintenance/*

# RUN mv .usr/local/bin/maintenance/* /usr/local/bin \
#     && rmdir /usr/local/bin/maintenance


# FROM postgres:15-bullseye


# COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance

# RUN chmod +x /usr/local/bin/maintenance/*

# RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
#   && rmdir /usr/local/bin/maintenance


FROM postgres:15-bullseye
 
 
COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance
RUN sed -i 's/\r$//g' usr/local/bin/maintenance/_sourced/*
RUN sed -i 's/\r$//g' usr/local/bin/maintenance/backup
RUN sed -i 's/\r$//g' usr/local/bin/maintenance/backups
RUN sed -i 's/\r$//g' usr/local/bin/maintenance/restore
RUN chmod +x /usr/local/bin/maintenance/*
 
RUN mv /usr/local/bin/maintenance/* /usr/local/bin/ \
  && rmdir /usr/local/bin/maintenance