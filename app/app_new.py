#!/usr/bin/env python3

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pprint import pprint
from flask import Flask
import os

app = Flask(__name__)

username = os.environ.get('MONGODB_USERNAME')
password = os.environ.get('MONGODB_PASSWORD')
endpoint = os.environ.get('MONGODB_HOSTNAME')

# tlsCAFile = ''
# tlsCertificateKeyFile = ''

# uri = "mongodb+srv://%s:%s@%s/?tls=true" % (username, password, endpoint)
# skip_uri = uri + "&tlsAllowInvalidCertificates=true"
# tls_uri = uri + "&tlsCAFile=%s&tlsCertificateKeyFile=%s" % (tlsCAFile, tlsCertificateKeyFile)
# client = MongoClient(uri)


@app.route('/')
def mongo_client():
    client = MongoClient(endpoint,
                     27017,
                     username=username,
                     password=password)
                        #  tls=False,
                        #  tlsCAFile=tlsCAFile,
                        #  tlsCertificateKeyFile=tlsCertificateKeyFile,
                        #  tlsAllowInvalidCertificates=True)
    try:
        client.admin.command('ismaster')
    except ConnectionFailure:
        print("Server not available")

    db = client.admin
    pprint(db)
    serverStatusResult = db.command("serverStatus")
    pprint(serverStatusResult)
    return str(db) + str(serverStatusResult)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)