// demo: CAN-BUS Shield, send data
#include <mcp_can.h>
#include <SPI.h>
#include <Wire.h> //Arduino library for I2C communication

const int MPU_addr=0x68;
int16_t AcX,AcY,AcZ,Tmp; 

void setup()
{
  Wire.begin(); //setup I2C
  Wire.beginTransmission(MPU_addr); //prepare to write a command to sensor
  Wire.write(0x6B);  // PWR_MGMT_1 register
  Wire.write(0);     // set to zero (command to wake up the MPU-6050) 
  Wire.endTransmission(true); //close communication between Arduino (master) and MPU6050 (slave)
  Serial.begin(115200);
  // init can bus, baudrate: 500k
  if(CAN.begin(CAN_500KBPS) ==CAN_OK) Serial.print("can init ok!!\r\n");
  else Serial.print("Can init fail!!\r\n");
}

unsigned char stmp[2] = {0, 1};
void loop()
{
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false); 
  Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  Tmp=Wire.read()<<8|Wire.read();  // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
  Serial.print(Tmp/340.00+36.53); Serial.print(" ");
  memcpy(stmp, &Tmp, 2);
  //int16_t phil = (int16_t)(stmp[1]<<8 + stmp[0]);
  Serial.println(Tmp, HEX);Serial.print("\t");
  //Serial.println((int16_t)(stmp[1]<<8 + stmp[0])); 
  // send data:  id = 0x00, standrad flame, data len = 8, stmp: data buf
 CAN.sendMsgBuf(0x00, 0, 2, stmp);  
 delay(5000);                       // send data per 100ms
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
