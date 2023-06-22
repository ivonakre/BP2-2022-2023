from model import *
from model.relacije import *
from model.cache import region
from flask import Flask, request, render_template
from flask import jsonify
import json
from kafka import KafkaProducer, KafkaConsumer
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import threading

#naziv app koja se pokreće
#python -m flask run -> http://127.0.0.1:5000/ - iz classes.html
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

def json_deserializer(data):
    return json.loads(data)

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=json_serializer
)

consumer = KafkaConsumer(
    'gost',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=json_deserializer,
    group_id='test-group',
    auto_offset_reset='earliest'
)

kafka_thread = None

#/ korijenska ruta
@app.route("/")
#index naziv rute
def index ():
    classes = session.query(Gost).all()
    return render_template('classes.html', classes=classes)

@app.route("/classes/delete/<int:id_gost>", methods=["DELETE"])
def delete_class(id_gost):
    # ID se sada prenosi putem URL-a
    # Dohvati objekt Gost sa navedenim ID-om
    gost = session.query(Gost).get(id_gost)

    if gost:  # ako Gost s ovim ID-om postoji
        session.delete(gost)
        session.commit()
        # Uspješno izbrisano
        return jsonify({'message': f'Gost sa ID {id_gost} je izbrisan.'}), 200
    else:
        # Nema Gosta s ovim ID-om
        return jsonify({'message': f'Nema gosta s ID {id_gost}.'}), 404

@app.route("/classes/<int:id_gost>", methods=["GET"])
def get_class(id_gost):
    gost = region.get_or_create(
        f'Gost:{id_gost}', 
        creator=lambda: session.query(Gost).get(id_gost),
        expiration_time=60  # The time after which to expire the cache
    )
    if gost:
        # pretvoriti objekt Gost u rječnik
        # Uspješno dohvaćeno
        return jsonify([{"ID_gost": gost.ID_gost, "ime": gost.ime, "prezime": gost.prezime, "spol": gost.spol, "godiste": gost.godiste, "adresa": gost.adresa}]), 200
    else:
        # Nema Gosta s ovim ID-om
        return jsonify({'message': f'Nema gosta s ID {id_gost}.'}), 404

@app.route("/classes/edit", methods=["PUT"])
def edit_class():
    id_gost = request.form.get("ID_gost")
    ime = request.form.get("ime")
    prezime = request.form.get("prezime")
    spol = request.form.get("spol")
    godiste = request.form.get("godiste")
    adresa = request.form.get("adresa")

    if id_gost:  
        # Dohvati objekt Gost sa navedenim ID-om
        gost = session.query(Gost).get(id_gost)
        if gost:  # ako Gost s ovim ID-om postoji
            # Ažurirati atribute objekta Gost
            if ime: 
                gost.ime = ime
            if prezime: 
                gost.prezime = prezime
            if spol: 
                gost.spol = spol
            if godiste: 
                gost.godiste = godiste
            if adresa: 
                gost.adresa = adresa
            
            session.commit()

            producer.send("gost", [{"ID_gost": gost.ID_gost, "ime": gost.ime, "prezime": gost.prezime, "spol": gost.spol, "godiste": gost.godiste, "adresa": gost.adresa}])
            producer.flush()

            # Uspješno ažurirano
            return jsonify({'message': f'Gost sa ID {id_gost} je ažuriran.'}), 200
        else:
            # Nema Gosta s ovim ID-om
            return jsonify({'message': f'Nema gosta s ID {id_gost}.'}), 404
    else:
        # Nije pružen ID
        return jsonify({'message': 'ID nije pružen.'}), 400

@app.route("/classes/add", methods=["POST"])
def add_class():
    # Dohvati 'ime', 'prezime', 'spol', 'godiste' i 'adresa'
    ime = request.form.get("ime")
    prezime = request.form.get("prezime")
    spol = request.form.get("spol")
    godiste = request.form.get("godiste")
    adresa = request.form.get("adresa")
    
    # Dodaj novi gost
    gost = Gost(ime=ime, prezime=prezime, spol=spol, godiste=godiste, adresa=adresa)
    session.add(gost)
    session.commit()

    producer.send("gost", [{"ID_gost": gost.ID_gost, "ime": gost.ime, "prezime": gost.prezime, "spol": gost.spol, "godiste": gost.godiste, "adresa": gost.adresa}])
    producer.flush()

    # Dobra je praksa vratiti ispravan JSON zahtjev
    return jsonify({'message': 'Dodan novi gost u bazu.'})

@socketio.on('connect', namespace='/kafka')
def connect():
    global kafka_thread
    if kafka_thread is None or not kafka_thread.is_alive():
        kafka_thread = threading.Thread(target=kafka_consumer)
        kafka_thread.start()

def kafka_consumer():
    for poruka in consumer:
        gost = poruka.value
        socketio.emit('data', {'gost': gost}, namespace='/kafka')

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True)