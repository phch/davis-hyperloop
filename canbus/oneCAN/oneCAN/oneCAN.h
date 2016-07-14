#ifndef oneCAN_h
#define oneCAN_h
#include <Arduino.h>
#include <SPI.h>
#include <mcp_can.h>
#include <mcp_can_dfs.h>

const unsigned int CAN_motionData = 0x4;
const unsigned int CAN_accelData = 0x5;
const unsigned int CAN_controlsHeartbeat = 0x1;
const unsigned int CAN_emergencyHeartbeat = 0x2;
const unsigned int CAN_RRPEHeartbeat = 0x3;
const unsigned long CAN_heartbeatPeriod = 10000;

void CAN_getData (void);

class oneCAN
{
	public:
		oneCAN(void);
		void init(void);
		void beginReceiving(void);
		void sendFloatData(unsigned int dataType, float f1, float f2);
		void sendIntData(unsigned int dataType, int i1, int i2);
		void beat(unsigned int systemID);
		volatile float velocity;
		volatile float position;
		volatile float accelAngleX;
		volatile float accelAngleY;
		void getData(void);
		bool areControlsOn(void);
		bool isEmergencyOn(void);
		bool isRRPEOn(void);
		static oneCAN* getActive(void);
	private:
		unsigned char len = 0;
		unsigned char buf[8];
		unsigned long controlsHeartbeatTime = 0;
		unsigned long emergencyHeartbeatTime = 0;
		unsigned long RRPEHeartbeatTime = 0;
		static oneCAN* active;
};
#endif