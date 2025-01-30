FROM openjdk:17-slim

WORKDIR /fuseki

# Copiază toate fișierele Fuseki în container
COPY app /fuseki

RUN chmod +x ./fuseki-server

# Expune portul standard pentru SPARQL
EXPOSE ${PORT}

# Setează comanda de rulare a serverului
CMD ["sh", "-c", "./fuseki-server --port $PORT"]
#merge in heroookuuuud