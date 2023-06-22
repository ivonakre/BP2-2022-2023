from confluent_kafka import Producer
import json

kafka_conf = {
    "bootstrap.servers" : "kafka:9092"
}

producer = Producer(kafka_conf)

gost = {
    "ime" : "pero",
    "prezime" : "peric",
    "spol" : "musko",
    "godiste" : "2000",
    "adresa": "a"
}

gost_json = json.dumps(gost)

producer.produce("topic_gost", gost_json)

producer.flush()