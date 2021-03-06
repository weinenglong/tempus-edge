package com.hashmapinc.tempus.edge.opcTagFilter

import collection.JavaConverters._

import com.iotracks.elements.IOMessage
import com.typesafe.scalalogging.Logger

import com.hashmapinc.tempus.edge.proto.{MessageProtocols, ConfigMessageTypes, DataMessageTypes}

/**
 * This object holds the async logic for handling iofog events
 */
object IofogController extends com.hashmapinc.tempus.edge.iofog.IofogController {
  val log = Logger(getClass())

  /**
   * Handles new messages
   *
   * @param messages - list of received messages
   */
  def onMessages(
    messages: java.util.List[IOMessage]
  ): Unit = {
    // handle messages based on message type
    messages.asScala.map((msg) => {
      try {
        // determine if message is a CONFIG message
        val msgContent  = msg.getContentData
        val msgProtocol = msgContent(0) 
        val msgType     = msgContent(1) 

        // handle config update alerts
        if (
          msgProtocol == MessageProtocols.CONFIG.value.toByte && 
          msgType     == ConfigMessageTypes.UPDATE_ALERT.value.toByte
        ) {
          Config.updateConfigs
          OpcController.updateSubscriptions
        }
        else 
          log.error("Could not handle message with protocol " + msgProtocol + " and type " + msgType)
      } catch {
        case e: Exception => log.error("Error trying to parse iofog message: " + e)
      }
    })
  }
}