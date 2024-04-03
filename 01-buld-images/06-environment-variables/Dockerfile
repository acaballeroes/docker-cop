FROM mcr.microsoft.com/mssql/server:2019-latest

ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=YourStrongPassword123

RUN mkdir -p /var/opt/mssql/data

CMD ["/opt/mssql/bin/sqlservr"]