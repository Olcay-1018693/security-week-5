# Encryptie/Decryptie App

Deze applicatie biedt de mogelijkheid om tekst te versleutelen en te ontsleutelen met behulp van symmetrische encryptie. De app maakt gebruik van de `cryptography`-bibliotheek en Flask voor de webinterface.

## Functionaliteiten
* Versleutelen van tekst
* Ontsleutelen van versleutelde tekst
* Webinterface gebouwd met Flask
* Symmetrische encryptie met behulp van `cryptography.fernet`

## Vereisten
Om deze applicatie lokaal te draaien, moet je ervoor zorgen dat de volgende afhankelijkheden geïnstalleerd zijn:

* Python 3.x
* Flask
* Cryptography

## Dependencies
De belangrijkste pakketten die worden gebruikt zijn:

* Flask: Voor de webinterface
* Cryptography: Voor de encryptie en decryptie

## Installatie en Setup
1. Clone de repository:
    ```bash
    git clone https://github.com/Olcay-1018693/security-week-5.git
    cd security-week-5
    ```

2. Installeer de vereisten met:
    ```bash
    pip install -r requirements.txt
    ```

3. Genereer een encryptiesleutel:

    De applicatie gebruikt een sleutel voor de encryptie. Voer het volgende commando uit om de sleutel eenmalig te genereren:

    ```bash
    python generate_key.py
    ```
    Dit genereert een bestand `secret.key` dat wordt gebruikt voor de encryptie en decryptie van berichten.

4. Start de Flask-server:

    Je kunt nu de applicatie starten door de Flask-server te draaien:

    ```bash
    python app.py
    ```
5. Open de app in je browser:

    Ga naar http://127.0.0.1:5000/ om de webinterface te gebruiken.

## Gebruik
1. **Versleutelen**:

   * Voer een tekst in het formulier "Versleutelen" en klik op de knop "Versleutel".
   * De versleutelde tekst zal onder het formulier verschijnen.

2. **Ontsleutelen**:

    * Voer een versleutelde tekst in het formulier "Ontsleutelen" en klik op de knop "Ontsleutel".
    * De ontsleutelde tekst zal onder het formulier verschijnen.

## Documentatie
### Encryptie
De applicatie gebruikt `cryptography.fernet` voor symmetrische encryptie. Dit betekent dat dezelfde sleutel wordt gebruikt om zowel te versleutelen als te ontsleutelen. De sleutel wordt eenmalig gegenereerd en opgeslagen in het bestand `secret.key`.

### Decryptie
De versleutelde tekst kan ontsleuteld worden door de originele sleutel te gebruiken. Zorg ervoor dat het bestand `secret.key` niet verloren gaat, want zonder deze sleutel kan de tekst niet ontsleuteld worden.
