import paho.mqtt.client as mqtt_sender
import json
from random import randint
from loguru import logger
from env import *
from devices.ahu import ahu_logic, ahu_stop, start_ahu, ahu_set_season
from devices.cool_center import cooling_center, pump_ch_control
from devices.cool_water_counter import cool_water
from devices.drain_station import drain_station
from devices.electro_counter import electro_counter
from devices.grp import grp
from devices.heat_counter import heat_en_counter
from devices.heat_water_counter import heat_water
from devices.itp import itp, pump_control
from devices.lift import lift
from devices.ligth import light, all_on, all_off, random_light
from devices.scud import scud
from devices.water_station import pump_station


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.debug("SENDER connection SUCCESS!")
    else:
        logger.error(f"SENDER connection FAIL - CODE: {rc}")
    return rc


send_mqtt = mqtt_sender.Client(client_id=PUBLISHER + str(randint(1234, 56789)), clean_session=True,
                               userdata=None, protocol=mqtt_sender.MQTTv311, transport=TRANSPORT)
send_mqtt.ws_set_options(path=PATH, headers=None)
send_mqtt.username_pw_set(USER_NAME, password=USER_PASS)


def publish(device):
    send_json = json.dumps(device)
    send_mqtt.publish(f"emulator/{device['name']}", payload=send_json, qos=QOS, retain=RETAIN)
    logger.info(f'Sending json: {send_json}')


def run_emulator():
    logger.debug('Run SENDER')
    try:
        send_mqtt.connect(HOST, port=PORT, keepalive=60, bind_address="")
        logger.debug("Sender is connected!")
    except Exception as e:
        logger.exception("Sender FAIL connect to broker", e)
    publish(ahu_logic())
    publish(cooling_center())
    publish(cool_water())
    publish(drain_station())
    publish(electro_counter())
    publish(heat_en_counter())
    publish(grp())
    publish(heat_water())
    publish(itp())
    publish(lift())
    publish(light())
    publish(scud())
    publish(pump_station())
    send_mqtt.disconnect()


def control(topic, json_data):
    if 'ahu' in topic:
        logger.info("DO control AHU")
        ahu_control(json_data)
    if 'light' in topic:
        logger.info("DO control Light")
        light_control(json_data)
    if 'itp' in topic:
        logger.info("DO control ITP")
        itp_control(json_data)
    if 'chiller' in topic:
        logger.info("DO control Chiller-Center")
        chiller_control(json_data)


def ahu_control(json_data):
    if 'mode' in json_data.keys():
        if json_data['mode'] == 1:
            logger.debug("Start ahu")
            publish(start_ahu())
        else:
            logger.debug("Stop ahu")
            publish(ahu_stop())
    if 'season' in json_data.keys():
        if json_data['season'] in (1, 2):
            logger.debug("Set season-mode ahu")
            publish(ahu_set_season(json_data['season']))
            publish(ahu_logic())
    if 'set-temp' in json_data.keys():
        # TODO
        logger.debug("Set season-mode ahu")
        pass


def light_control(json_data):
    if 'mode' in json_data.keys():
        if json_data['mode'] == 1:
            logger.debug("All light ON")
            publish(all_on())
        if json_data['mode'] == 2:
            logger.debug("All light OFF")
            publish(all_off())
        if json_data['mode'] == 3:
            logger.debug("Light random")
            publish(random_light())


def itp_control(json_data):
    if 'pump-1' in json_data.keys():
        pump_control('pump-1', json_data['pump-1'])
    if 'pump-2' in json_data.keys():
        pump_control('pump-2', json_data['pump-2'])
    if 'pump-3' in json_data.keys():
        pump_control('pump-3', json_data['pump-3'])
    if 'pump-4' in json_data.keys():
        pump_control('pump-4', json_data['pump-4'])


def chiller_control(json_data):
    if 'nc1' in json_data.keys():
        pump_ch_control('nc1', json_data['nc1'])
    if 'nc2' in json_data.keys():
        pump_ch_control('nc2', json_data['nc2'])
    if 'nc3' in json_data.keys():
        pump_control('nc3', json_data['nc3'])
    if 'nc4' in json_data.keys():
        pump_ch_control('nc4', json_data['nc4'])
