from random import randint
import paho.mqtt.client as mqtt_client
from loguru import logger
import json
from sender import run_emulator, control
from env import *

subscribe_list = [("command/ahu", QOS), ("command/light", QOS), ("command/itp", QOS), ("command/chiller", QOS)]


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.debug("Connection success!")
        mqtt.subscribe(subscribe_list)
    else:
        logger.error(f"Connection fail - CODE: {rc}")
    return rc


def on_message(client, userdata, msg):
    topic = msg.topic
    data = str(msg.payload.decode("utf-8"))
    logger.debug(topic, '\n', str(data))
    command_data = json.loads(data)
    control(topic, command_data)


mqtt = mqtt_client.Client(client_id=PUBLISHER + str(randint(1234, 56789)), clean_session=True, userdata=None,
                          protocol=mqtt_client.MQTTv311, transport=TRANSPORT)
mqtt.ws_set_options(path=PATH, headers=None)
mqtt.username_pw_set(USER_NAME, password=USER_PASS)
mqtt.on_connect = on_connect
mqtt.on_message = on_message

rc = mqtt.connect(HOST, port=PORT, keepalive=3600, bind_address="")
if rc == 0:
    while True:
        if rc == 0:
            run_emulator()
            loop_code = mqtt.loop(timeout=5.0)
            logger.debug(f"loop_code: {loop_code}")
            if loop_code != 0:
                rc = mqtt.connect(HOST, port=PORT, keepalive=60, bind_address="")
