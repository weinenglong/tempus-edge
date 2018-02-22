package com.hashmapinc.tempus.clientdevice.edgeconfig.mqtt;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.hashmapinc.tempus.clientdevice.ApplicationConstants;
import com.hashmapinc.tempus.clientdevice.edgeconfig.ConfigMessageHandler;
import org.apache.log4j.Logger;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class TempusMqttCallback implements MqttCallback{
    ConfigMessageHandler configMessageHandler;
    MqttManager client;
    final static Logger logger = Logger.getLogger(MqttCallback.class);
    public TempusMqttCallback(ConfigMessageHandler configMessageHandler,MqttManager client)
    {
        this.configMessageHandler=configMessageHandler;
        this.client=client;
    }
    @Override
    public void connectionLost(Throwable throwable) {
        logger.info("Connection lost with Mqtt reconnecting");
        client.start();
    }

    @Override
    public void messageArrived(String s, MqttMessage mqttMessage) throws Exception {
        logger.info("New message arrived");
        String stringMsg=new String(mqttMessage.getPayload()).replaceAll("\\\\n", "");
        stringMsg=stringMsg.replaceAll("\\\\t","");
        logger.debug("Incomming message "+stringMsg);
        Gson gson = new Gson();
        JsonObject jsonConfig = gson.fromJson(stringMsg, com.google.gson.JsonObject.class);
        if(jsonConfig.has(ApplicationConstants.SHARED))
        {
            jsonConfig=jsonConfig.getAsJsonObject(ApplicationConstants.SHARED);
        }
        if(jsonConfig.has(ApplicationConstants.CONFIG_PARAM)) {
            String stringConfig = jsonConfig.get(ApplicationConstants.CONFIG_PARAM).toString().replaceAll("\\\\", "");
            jsonConfig = gson.fromJson(stringConfig.substring(1, stringConfig.length() - 1), com.google.gson.JsonObject.class);
            for (String entry : jsonConfig.keySet()) {
                configMessageHandler.persistConfig(entry, jsonConfig.get(entry).toString());
            }
        }

    }

    @Override
    public void deliveryComplete(IMqttDeliveryToken iMqttDeliveryToken) {

    }

}
