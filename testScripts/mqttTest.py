import paho.mqtt.client as mqtt
import datetime

username = "xxx"
password = "xxx"
client_id = "Python Test"
clean_session = False

mqttc = mqtt.Client(client_id, clean_session)
mqttc.username_pw_set(username, password)


mqttc.connect("m21.cloudmqtt.com", 17472)
mqttc.loop_start()

test_message = "Test Message"
current_time = datetime.datetime.now().time()
current_time.isoformat()

mqttc.publish("paho/messages", test_message, 1)
mqttc.publish("paho/lastudate", str(current_time), 1, True)
mqttc.disconnect()
