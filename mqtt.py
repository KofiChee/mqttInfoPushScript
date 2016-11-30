import paho.mqtt.client as mqtt
import datetime
import psutil
import math


def get_uptime():
    """
    Returns the boot time of the system, formated as days, hours,
    minutes and seconds. psutil.boot_time() returns the boot time
    in epoch seconds, so we subtract that from the current time
    in epoch seconds

    We then convert back using divmod, which does modulus on the
    first argument by the second,then returns a tuple of the
    modulus followed by the remainder
    """
    seconds = datetime.datetime.now().timestamp() - psutil.boot_time()
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return '{} days, {} hours, {}} minutes, \
            {} seconds'.format(int(d), int(h), int(m), int(s))


def get_cpu_load():
    """
    We use the argument 2 here, which is the interval the psutil.cpu_percent()
    checks for. This is not too low as to return an incorrect number,
    but not too high as it is a blocking process
    """
    return psutil.cpu_percent(2)


def get_free_memory():
    """
    psutil.virtual_memory() returns a named_tuple full of information about
    virtual memory. For the purposes of this script, we are only interested in
    free memory, which is at  memory[4]
    """
    memory = psutil.virtual_memory()
    free_memory = memory[4] / 1024 ** 2
    return math.floor(free_memory)


def get_free_storage():
    """
    This functions very similarly to get_free_memory above, only that
    psutil.disk_usage('/') provides info about the root filesystem instead
    of virtual memory.
    In this instance, we are interested only in free space, which is at [2]
    On windows this reports free space on the OS drive
    """
    storage = psutil.disk_usage('/')
    free_space = storage[2] / 1024 ** 2
    return math.floor(free_space)


def get_net_info():
    """
    This function works similarly again to get_free_memory() and
    get_free_storage(), psutil.net_io_counters() returns a namedTuple,
    we are interested in netInfo[0] and netInfo[1].
    These indexes contain data sent in bytes and data received in bytes
    """
    netInfo = psutil.net_io_counters()

    mbSent = netInfo[0] / 1024 ** 2
    mbRec = netInfo[1] / 1024 ** 2

    return math.floor(mbSent), math.floor(mbRec)

print(get_uptime())
print(get_cpu_load())
print(get_free_memory())
print(get_free_storage())
print(get_net_info())


username = "bancbrxq"
password = "UFLIsH2raojY"
client_id = "System Test"
clean_session = False

mqttc = mqtt.Client(client_id, clean_session)
mqttc.username_pw_set(username, password)

mqttc.connect("m21.cloudmqtt.com", 17472)
mqttc.loop_start()


# This stores a datetime object in CT, which we then format
ct = datetime.datetime.now()
current_time = ct.strftime("%D - %H:%M:%S")

uptime = get_uptime()
cpu_load = get_cpu_load()
free_mem = get_free_memory()
free_storage = get_free_storage()
mb_sent, mb_received = get_net_info()


mqttc.publish("systemhealth/uptime", uptime, 1, True)
mqttc.publish("systemhealth/cpuload", cpu_load, 1, True)
mqttc.publish("systemhealth/freememory", free_mem, 1, True)
mqttc.publish("systemhealth/freestorage", free_storage, 1, True)
mqttc.publish("systemhealth/netsent", mb_sent, 1, True)
mqttc.publish("systemhealth/netreceived", mb_received, 1, True)
mqttc.publish("systemhealth/lastupdate", current_time, 1, True)
mqttc.disconnect()
