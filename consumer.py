from confluent_kafka import Consumer
import json
from model import *
from model.relacije import *

kafka_conf = {
    "bootstrap.servers" : "localhost:9092",
    "group.id" : "mojagrupa",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(kafka_conf)

consumer.subscribe(["topic_gost"])

while True:
    message = consumer.poll(1.0)
    if message:
        gost = json.loads(message.value().decode("utf8"))
        print(gost)
        db_gost = Gost(ime=gost["ime"], prezime=gost["prezime"], spol=gost["spol"], godiste=gost["godiste"], adresa=gost["adresa"])
        session.add(db_gost)
        session.commit()

consumer.close()