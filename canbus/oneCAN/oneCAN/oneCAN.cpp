#include "oneCAN.h"

oneCAN* oneCAN::active = 0;
MCP_CAN CAN(9);

oneCAN::oneCAN(void)
{
	active = this;
	dataAvailable = false;
}

void  oneCAN::init(void)
{
	// init can bus, baudrate: 100k
	if(CAN.begin(CAN_100KBPS) ==CAN_OK) Serial.print("CAN init ok!!\r\n");
	else Serial.print("CAN init fail!!\r\n");
}

void oneCAN::sendFloatData(unsigned int dataType, float f1, float f2)
{ 
  //turn floats into a CAN compatible char array
  
  unsigned char* f1_CAN = (unsigned char*)&f1;
  unsigned char* f2_CAN = (unsigned char*)&f2;
  unsigned char f_CAN[8] = {0,0,0,0,0,0,0,0};
  
  for (int i=0; i<4; i++)
  {
    f_CAN[i] = *(f1_CAN+i);
    f_CAN[i+4] = *(f2_CAN+i);
  }
  
  //send data over CAN bus
  
  CAN.sendMsgBuf(dataType, 0, 8, f_CAN);
}

void oneCAN::sendIntData(unsigned int dataType, int i1, int i2)
{ 
  //turn ints into a CAN compatible char array
  
  unsigned char* i1_CAN = (unsigned char*)&i1;
  unsigned char* i2_CAN = (unsigned char*)&i2;
  unsigned char i_CAN[8] = {0,0,0,0,0,0,0,0};
  
  for (int i=0; i<4; i++)
  {
    i_CAN[i] = *(i1_CAN+i);
    i_CAN[i+4] = *(i2_CAN+i);
  }
  
  //send data over CAN bus
  
  CAN.sendMsgBuf(dataType, 0, 8, i_CAN);
}

void oneCAN::beat(unsigned int systemID)
{ 
	unsigned char beatMessage[1] = {0x0};
	CAN.sendMsgBuf(systemID, 0, 1, beatMessage);
	Serial.println("Heartbeat sent!");
}

void oneCAN::beginReceiving(void)
{
	attachInterrupt(0, CAN_setDataAvailable, FALLING);
}

void CAN_setDataAvailable (void)
{
	oneCAN::getActive()->dataAvailable = true;
}

oneCAN* oneCAN::getActive(void)
{
	return active;
}

void oneCAN::getData(void)
{
	 CAN.readMsgBuf(&this->len, this->buf);    // read data,  len: data length, buf: data buf
      int incomingDataType = CAN.getCanId();
      
      //Print data to the serial console 
      Serial.println("CAN_BUS GET DATA!");
      Serial.print("CAN ID: ");
      Serial.println(incomingDataType);
      Serial.print("data len = ");Serial.println(this->len);
      
      //This loops through each byte of data and prints it
      for(int i = 0; i<this->len; i++)    // print the data
      {
        Serial.print(this->buf[i]);Serial.print("\t");
      }
      Serial.println();
      
      //check type of CAN data and upade variables accordingly
      
      switch (incomingDataType)
      {
        case CAN_motionData:
          this->velocity = *(float *)this->buf;
          this->position = *(float *)(this->buf+4);
          
          Serial.print("Motion data received! New velocity: ");
          Serial.print(this->velocity);
          Serial.print(" New position: ");
          Serial.println(this->position);
          Serial.println();
          break;
          
	   case CAN_accelData:
		this->accelAngleX = *(float *)this->buf;
          this->accelAngleY = *(float *)(this->buf+4);
          
          Serial.print("Accelerometer data received! New X angle: ");
          Serial.print(this->accelAngleX);
          Serial.print(" New Y angle: ");
          Serial.println(this->accelAngleY);
          Serial.println();
          break;
          
        case CAN_controlsHeartbeat:
        	controlsHeartbeatTime = millis();
        	Serial.println("Control heartbeat detected!");
        	break;
        	
        case CAN_emergencyHeartbeat:
        	emergencyHeartbeatTime = millis();
        	Serial.println("Emergency heartbeat detected!");
        	break;
        	
        case CAN_RRPEHeartbeat:
        	RRPEHeartbeatTime = millis();
        	Serial.println("RRPE heartbeat detected!");
        	break;
        	
        default:
          Serial.println("Error: Unrecognized CAN ID");
          break;
      }
}

bool oneCAN::areControlsOn(void)
{
	return (millis() - controlsHeartbeatTime) < CAN_heartbeatPeriod;
}

bool oneCAN::isEmergencyOn(void)
{
	return (millis() - emergencyHeartbeatTime) < CAN_heartbeatPeriod;
}

bool oneCAN::isRRPEOn(void)
{
	return (millis() - RRPEHeartbeatTime) < CAN_heartbeatPeriod;
}