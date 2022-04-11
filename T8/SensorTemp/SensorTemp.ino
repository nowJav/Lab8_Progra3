
int Sensor = 0 ;
int umbral = 25 ;

void setup()
{
  Serial.begin(9600);
}

void loop ()
{
  int lectura = analogRead(Sensor);
  float voltaje = 5.0 /1024 * lectura ; // Atencion aqui
            // Si usais un LM35DZ vuestra formula sera
            //float temp = voltaje * 100 ;
  float temp = voltaje * 100 -50 ; 
  Serial.println(temp) ; delay(1000); 
}
/*
#define Sensor A0
#define Led1 11
#define Led2 12
#define Led3 13

int umbral = 25 ;
int hot = 35; //set hot parameter
int cold = 25; //set cold parameter
void setup() {
pinMode(Sensor, INPUT); //sensor
pinMode(Led1, OUTPUT); //blue
pinMode(Led2, OUTPUT); //green
pinMode(Led3, OUTPUT); //red
Serial.begin(9600);
}
void loop() {
 int sensor = analogRead(Sensor);
  float voltaje = 5.0 /1024 * sensor ; // Atencion aqui
            // Si usais un LM35DZ vuestra formula sera
            //float temp = voltaje * 100 ;
  float temp = voltaje * 100 -50 ; 
  Serial.println(temp);
if (temp < cold) { //cold
digitalWrite(Led1, HIGH);
digitalWrite(Led2, LOW);
digitalWrite(Led3, LOW);
//Serial.println(" It's Cold.");
}
else if (temp >= hot) { //hot
digitalWrite(Led1, LOW);
digitalWrite(Led2, LOW);
digitalWrite(Led3, HIGH);
//Serial.println(" It's Hot.");
}
else { //fine
digitalWrite(Led1, LOW);
digitalWrite(Led2, HIGH);
digitalWrite(Led3, LOW);
//Serial.println(" It's Fine.");
}
delay(1000);
}*/
