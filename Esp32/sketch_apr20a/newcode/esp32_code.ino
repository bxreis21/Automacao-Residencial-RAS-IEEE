#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "Nibos_Ana Xavier _2.4G";
const char* password = "17231976";

void setup() {
  Serial.begin(9600);

  pinMode(15,OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
  pinMode(21, OUTPUT);
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);

  WiFi.begin(ssid, password);
  Serial.print("Conectando ao WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(200);
    Serial.print(".");
  }
  Serial.println("Conectado!");
}

void loop() {

  HTTPClient http;
  http.begin("http://192.168.1.7:8000/api_devices");
  int httpCode = http.GET();

  if (httpCode == HTTP_CODE_OK) {

    String jsonString = http.getString();
    jsonString.remove(0,1);
    jsonString.remove(jsonString.length()-1,1);
    jsonString.replace("\\","");

    DynamicJsonDocument doc(1024);
    DeserializationError error = deserializeJson(doc, jsonString);
    
    if (error) {
      Serial.print("Erro na deserialização: ");
      Serial.println(error.c_str());
      return;
    }

    for (JsonObject device : doc.as<JsonArray>()) {  
      //device id
      Serial.print("PK: ");
      Serial.println(device["pk"].as<int>());

      JsonObject fields = device["fields"];
      //device name
      Serial.print("Name: ");
      Serial.println(fields["name"].as<String>());
      //device status
      Serial.print("Status: ");
      Serial.println(fields["status"].as<bool>());

      device_function(fields["status"].as<bool>(), fields["porta"].as<int>());

      delay(100);
    }
  }

  else {
    Serial.println("Falha ao conectar com o servidor");
  }

  http.end();
}

void device_function(bool value, int door){
  if(value){
    digitalWrite(door, HIGH);
  }
  else {
    digitalWrite(door, LOW);
  }
}


