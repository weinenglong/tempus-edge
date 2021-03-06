package com.hashmapinc.tempus.edge.opcTagFilter

import scala.util.Try

import com.typesafe.scalalogging.Logger

import com.hashmapinc.tempus.edge.iofog.IofogConnection
import com.hashmapinc.tempus.edge.opc.OpcConnection

/**
 * Driver for the overall edge application
 *
 * @author randypitcherii
 */
object Driver {
  private val log = Logger(getClass())

  def main(
    args: Array[String]
  ): Unit = {
    log.info("Starting edge application driver...")
    log.info("CONTAINER_ID = " + IofogConnection.CONTAINER_ID)

    Config.updateConfigs                  // load initial configs.
    if (Config.trackConfig.isDefined) {
      OpcConnection.updateClient(Try(Config.trackConfig.get.getOpcConfig)) // init client connection.
      OpcController.updateSubscriptions   // look for subscriptions.
    }
      
    log.info("Connecting to iofog...")
    IofogConnection.connect(IofogController)
    log.info("iofog connection was successful. Listening...")
  }
}
