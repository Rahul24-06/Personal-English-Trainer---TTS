#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):
    sentence = 'You asked the meaning for  '

    if intent_message.intent.intent_name == '&PM84NKnAGk60OqRQDgeDerZPBkJDpx1m9abBvd5X:FindMeaning':
        print('FindMeaning')
#        sentence += 'the weather '
#    elif intent_message.intent.intent_name == 'searchWeatherForecastTemperature':
#        print('searchWeatherForecastTemperature')
#        sentence += 'the temperature '
    else:
        return

    givenword_slot = intent_message.slots.givenword.first()
#    forecast_locality_slot = intent_message.slots.forecast_locality.first()

    if givenword_slot is not None:
        sentence += givenword_slot.value
	
    if givenword_slot == 'Recuperate':
	sentence += 'The meaning of Recuperate is to recover from illness or exertion'
		
    # if forecast_country_slot is not None:
        # sentence += 'in ' + forecast_country_slot.value
    # if forecast_start_datetime_slot is not None and len(forecast_start_datetime_slot) > 0:
        # sentence += ' ' + forecast_start_datetime_slot[0].raw_value

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
