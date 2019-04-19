#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from hermes_python.hermes import Hermes
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR,str(MQTT_PORT))

def intent_received(hermes, intent_message):
        word = ''
        sentence = 'Sir, You asked the meaning for '
        if intent_message.intent.intent_name == '&PM84NKnAGk60OqRQDgeDerZPBkJDpx1m9abBvd5X:FindMeaning':
                print('FindMeaning')
        else:
                return

        givenword_slot = intent_message.slots.givenword.first()
        if givenword_slot is not None:
                sentence += givenword_slot.value
                word += givenword_slot.value
                print(word)
                sentence += '. The Meaning of ' + word + ' is, '

        if word == 'Recuperate':
                sentence += 'to recover from illness or exertion.'

        if word == 'anomaly':
                sentence += 'something that is unusual or unexpected. '
                sentence += 'For example: '
                sentence += 'The student’s poor performance on the latest test was an anomaly since she had previously earned excellent grades.'

        if word == 'equivocal':
                sentence += 'not easily understood or explained. '
                sentence += 'For example: '
                sentence += 'Politicians have been known to provide equivocal answers to reporters’ questions.'

		if word == 'lucid':
                sentence += 'very clear and easy to understand. '
                sentence += 'For example: '
                sentence += 'The lecture was lucid and straightforward, allowing the students to fully grasp the concepts presented.'

        if word == 'precipitate':
                sentence += 'to cause (something) to happen quickly or suddenly. '
                sentence += 'For example: '
                sentence += 'Unforeseen costs can precipitate a budget crisis.'

        if word == 'assuage':
                sentence += 'to make (an unpleasant feeling) less intense. '
                sentence += 'For example: '
                sentence += 'A massage can assuage the soreness in your muscles.'

        if word == 'erudite':
                sentence += 'having or showing great knowledge. '
                sentence += 'For example: '
                sentence += 'High school students often struggle with novels that are more erudite than they are entertaining.'

        if word == 'opaque':
                sentence += 'able to be seen through or not easily understood. '
                sentence += 'For example: '
                sentence += 'Medical jargon includes many opaque terms like macrosomic, which describes a newborn who weighs more than 4,000 grams.'

        if word == 'prodigal':
                sentence += 'wastefully extravagant. '
                sentence += 'For example: '
                sentence += 'The prodigal prince bought lavish gifts and planned expensive events.'

        if word == 'enigma':
                sentence += 'a person or thing that is mysterious, puzzling, or difficult to understand. '
                sentence += 'For example: '
                sentence += 'Scientists continue to research cancer to solve the enigma of its primary cause, which will hopefully lead to a cure.'

        if word == 'fervid':
                sentence += 'intensely enthusiastic or passionate. '
                sentence += 'For example: '
                sentence += 'The child showed a fervid fascination for superheroes, pouring over comic books for hours.'

        if word == 'placate':
                sentence += 'to make (someone) less angry or hostile. '
                sentence += 'For example: '
                sentence += 'A parent may decide to placate a baby with a pacifier.'

        if word == 'zeal':
                sentence += 'a strong feel of interest and enthusiasm that makes someone very eager or determined to do something. '
                sentence += 'For example: '
                sentence += 'The great emperor’s crusading zeal led him to conquer many lands.'

        if word == 'abstain':
                sentence += 'restrain oneself for doing or enjoying something. '
                sentence += 'For example: '
                sentence += 'Doctors encourage their patients to abstain from smoking cigarettes.'


        if word == 'audacious':
                sentence += 'a willingness to take bold risks or showing a lack of respect. '
                sentence += 'For example: '
                sentence += 'The new CEO pursued audacious initiatives to save the company from bankruptcy. / The student’s audacious remark earned her a se$

        if word == 'desiccate':
                sentence += 'remove the moisture from something. '
                sentence += 'For example: '
                sentence += 'The heat and energy from the sun can desiccate even the most hearty plants.'

        if word == 'gullible':
                sentence += 'easily persuaded to believe something. '
                sentence += 'For example: '
                sentence += 'The gullible little boy gave his older sister all of his allowance because she told him she would buy a pony for him.'

        if word == 'laudable':
                sentence += 'deserving praise and commendation. '
                sentence += 'For example: '
                sentence += 'Providing affordable healthcare for all citizens is a laudable goal.'

        if word == 'pedant':
                sentence += 'a person who makes an excessive display of learning. '
                sentence += 'For example: '
                sentence += 'Professor Blackwell, a well-known pedant, required his pre-med students to speak in Latin throughout the entire semester.'

        if word == 'vacillate':
                sentence += 'to waver between different opinions or actions. '
                sentence += 'For example: '
                sentence += 'Undergraduate students often vacillate among various majors before deciding which degree to pursue.'

        if word == 'adulterate':
                sentence += 'to make (something) impure or weaker by adding something of inferior quality. '
                sentence += 'For example: '
                sentence += 'Many chefs use fresh produce and refuse to adulterate their dishes with canned ingredients.'

        if word == 'capricious':
                sentence += 'given to sudden changes of mood or behavior. '
                sentence += 'For example: '
                sentence += 'The capricious supervisor would hand out raises one day and fire his entire staff the next.'


        if word == 'engender':
                sentence += 'to produce, cause, or give rise to (something).'
                sentence += 'For example: '
                sentence += 'Political debates can engender controversy regarding the subjects discussed.'

        if word == 'homogenous':
                sentence += 'of the same or similar kind. '
                sentence += 'For example: '
                sentence += 'There are very few truly homogenous cultures since social diversity is increasingly widespread.'

        if word == 'loquacious':
                sentence += 'tending to talk a great deal. '
                sentence += 'For example: '
                sentence += 'The loquacious professor was known for his five-hour lectures.'

        if word == 'pragmatic':
                sentence += 'dealing with the problems that exist in a reasonable and logical way instead of depending on theories. '
                sentence += 'For example: '
                sentence += 'A pragmatic approach to legislation can be difficult given the complexities of politics.'
        hermes.publish_end_session(intent_message.session_id, sentence)

with Hermes(MQTT_ADDR) as h:
        h.subscribe_intents(intent_received).start()
                                               
