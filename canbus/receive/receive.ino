// demo: CAN-BUS Shield, receive data
#include <mcp_can.h>
#include <SPI.h>

unsigned char Flag_Recv = 0;
unsigned char len = 0;
unsigned char buf[8];
char str[20];

void setup()
{
  attachInterrupt(0, MCP2515_ISR, FALLING);     // start interrupt
  Serial.begin(115200);
  if(CAN.begin(CAN_500KBPS) ==CAN_OK) Serial.print("can init ok!!\r\n"); else Serial.print("can init failed");  
}

void MCP2515_ISR()
{
    Flag_Recv = 1;
}

void loop()
{
  // order of operations not correct
  // total impedance: 60 ohms
  // ideally: 2 120 ohms at the end of the communication bus
  // read the CAN spec
  // CAN is broadcast
  // design own breakboard vs TI, or hack together something like Arduino?
  // lowest id is sent first, if same priority, send based on length of data
  // 
  
    if(Flag_Recv)                           // check if get data
    {
      Flag_Recv = 0;                        // clear flag
      CAN.readMsgBuf(&len, buf);            // read data,  len: data length, buf: data buf
      Serial.println("CAN_BUS GET DATA!");
      Serial.print("data len = ");
      Serial.println(len);

//      for(int i = 0; i<len; i++)            // print the data
//      {
          int16_t n = ((((int16_t) buf[1]) << 8) + ((int16_t) buf[0]));

            Serial.print(buf[1], HEX);
          
          Serial.print(buf[0], HEX);Serial.println("");
          
          Serial.print(n/340.0 + 36.53);Serial.print("\t");
//      }
      Serial.println();
    }
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
