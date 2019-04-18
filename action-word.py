#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):
        sentence = 'You asked the meaning for  '
        if intent_message.intent.intent_name == '&PM84NKnAGk60OqRQDgeDerZPBkJDpx1m9abBvd5X:FindMeaning':
        	print('FindMeaning')
        else:
                return
	givenword_slot = intent_message.slots.givenword.first()
        if givenword_slot is not None:
        	sentence += givenword_slot.value
		sentence += say + " Rahul "
	if givenword_slot == 'Recuperate':
		sentence += 'The meaning of Recuperate is to recover from illness or exertion'
        hermes.publish_end_session(intent_message.session_id, sentence)
	
with Hermes(MQTT_ADDR) as h:
        h.subscribe_intents(intent_received).start()
