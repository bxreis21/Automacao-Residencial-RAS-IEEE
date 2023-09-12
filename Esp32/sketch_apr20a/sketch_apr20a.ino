#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "Nibos_Ana Xavier _2.4G";
const char* password = "17231976";

int sala_luz_pk = 1 ;
int sala_ar_pk = 2 ;
int quarto_luz_pk = 3 ;
int quarto_ar_pk = 4 ;
int cozinha_luz_pk = 5 ;

void setup() {
  Serial.begin(9600);

  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);

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
  http.begin("http://192.168.1.4:8000/api_devices");
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
      Serial.print("pk: ");
      Serial.println(device["pk"].as<int>());

      JsonObject fields = device["fields"];
      //device name
      Serial.print("name: ");
      Serial.println(fields["name"].as<String>());
      //device status
      Serial.print("status: ");
      Serial.println(fields["status"].as<bool>());

      if(sala_luz_pk==device["pk"].as<int>()){
        sala_luz(fields["status"].as<bool>());
      }

      else if(sala_ar_pk==device["pk"].as<int>()){
        sala_ar_condicionado(fields["status"].as<bool>());
      }

      else if(quarto_luz_pk==device["pk"].as<int>()){
        quarto_luz(fields["status"].as<bool>());
      }

      else if(quarto_ar_pk==device["pk"].as<int>()){
        quarto_ar_condicionado(fields["status"].as<bool>());
      }

      else if(cozinha_luz_pk==device["pk"].as<int>()){
        cozinha_luz(fields["status"].as<bool>());
      }

      delay(100);
    }
  }

  else {
    Serial.println("Falha ao conectar com o servidor");
  }

  http.end();
}

void sala_luz(bool valor){
  if(valor){
    digitalWrite(2, HIGH);
  }
  else {
    digitalWrite(2, LOW);
  }
}

void sala_ar_condicionado(bool valor){
  if(valor){
    digitalWrite(4, HIGH);
  }
  else {
    digitalWrite(4, LOW);
  }
}

void quarto_luz(bool valor){
  if(valor){
    digitalWrite(5, HIGH);
  }
  else {
    digitalWrite(5, LOW);
  }
}

void quarto_ar_condicionado(bool valor){
  if(valor){
    digitalWrite(18, HIGH);
  }
  else {
    digitalWrite(18, LOW);
  }
}

void cozinha_luz(bool valor){
  if(valor){
    digitalWrite(19, HIGH);
  }
  else {
    digitalWrite(19, LOW);
  }
}
