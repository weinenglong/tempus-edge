package mqtt

import (
	"com/hashmapinc/tempus/edge/proto"
	"errors"
	"fmt"

	paho "github.com/eclipse/paho.mqtt.golang"
)

/*
onMessage parses the incoming msg and sends the parsed MqttMessage to the Inbox for processing.

This function is connected directly to the client through a paho.ClientOptions struct. This func
is called directly by the paho library.

@param msgClient 	- paho.Client that recieved the message.
@param msg 				- paho Message to process.
*/
func onMessage(msgClient paho.Client, msg paho.Message) {
	logger.Println("Received mqtt message!")

	// get qos
	var qos proto.MqttMessage_QoS
	switch msg.Qos() {
	case 0:
		qos = proto.MqttMessage_ZERO
	case 1:
		qos = proto.MqttMessage_ONE
	case 2:
		qos = proto.MqttMessage_TWO
	default:
		logger.Printf("received mqtt message with invalid QOS: %v\n", msg)
	}

	// convert msg to MqttMessage proto struct
	incomingMsg := &proto.MqttMessage{
		Qos:     qos,
		Payload: msg.Payload(),
		Topic:   msg.Topic(),
	}

	// send the parsed message to the inbox
	Inbox <- incomingMsg
}

/*
parseOptsFromConf creates a paho client options struct from the given mqttConfig

@param mqttConfig - pointer to the MqttConfig to use to create the paho client options

@returns opts - ClientOptions for creating a new paho client
*/
func parseOptsFromConf(mqttConfig *proto.MqttConfig) (opts *paho.ClientOptions, err error) {
	// perform light-weight config validation
	if mqttConfig == nil ||
		mqttConfig.Broker == nil ||
		len(mqttConfig.GetBroker().GetHost()) == 0 ||
		mqttConfig.GetBroker().GetPort() == 0 {

		err = errors.New("cannot parse nil mqttConfig into client options struct")
		return
	}

	// parse mqttConfig
	logger.Printf("Parsing mqttConf:\n%v\n into client options struct\n", mqttConfig)
	opts = paho.NewClientOptions().
		SetUsername(mqttConfig.GetUser().GetUsername()).
		SetPassword(mqttConfig.GetUser().GetPassword()).
		AddBroker(fmt.Sprintf("tcp://%s:%d", mqttConfig.GetBroker().GetHost(), mqttConfig.GetBroker().GetPort())).
		SetClientID("tempus::edge::mqtt")

	logger.Println("parsed opts:", opts)
	return
}

/*
createClient creates a paho client from the given mqttConfig

@param mqttConfig - pointer to the MqttConfig to use to create the paho client

@returns newClient - paho Client created from the mqttConfig
*/
func createClient(mqttConfig *proto.MqttConfig) (newClient paho.Client, err error) {
	// get paho client options from mqtt config
	opts, err := parseOptsFromConf(mqttConfig)
	if err != nil {
		return
	}

	// attach msg handler
	opts = opts.SetDefaultPublishHandler(onMessage)

	// return new client
	newClient = paho.NewClient(opts)
	return
}
