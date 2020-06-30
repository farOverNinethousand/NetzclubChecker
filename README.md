# Update 01.07.2020 - [Netzclub+ App eingestellt](https://www.teltarif.de/netzclub-plus-app-kostenlose-datenpakete-aenderungen/news/80899.html) --> Dieses Script hat leider nie wirklich funktioniert und spätestens jetzt ist es nutzlos. Laut Netzclub soll es in Zukunft jedoch weitere Möglichkeiten geben, an mehr gratis Datenvolumen zu kommen also immerhin ein Lichtblick. Dieses GitHub Projekt ist damit "gestorben" ;)

# NetzclubChecker
Script zum Prüfen von netzclub.net Accounts.
Zeigt den aktuell verbleibenden Traffic an ohne lästige Installation einer App.

### Installation
1. Installiere Python [Tutorial](https://gist.github.com/farOverNinethousand/2efc03be38c9932a338f1336fbef7977#python-installieren-windows)
2. Installiere die folgenden Python Module mit [dieser Anleitung](https://gist.github.com/farOverNinethousand/2efc03be38c9932a338f1336fbef7977#python-module-installieren-windows):  
`` requests ``
3. Lade dieses Projekt herunter und entpacke es.

### Verwendung
Starte die Checker.py und folge den Anweisungen.
Du musst dein [netzclub.net](https://www.netzclub.net/login/)  Passwort nicht zwingend eingeben, aber ohne dieses kann der bereits verbrauchte Traffic nicht angezeigt werden.
Beim ersten Start musst du eine Bestätigungs-SMS eingeben.
Du solltest das Script 2-3x pro Tag starten um zu gewährleisten, dass deine Session aktiv bleibt.  
Hierzu kann auch die automate.py hilfreich sein (siehe unten).  
Wenn alles ohne Probleme funktioniert solltest du in etwa folgendes sehen:
```
***************************************************************************
[netzclub] Traffic left: 299MB/300MB
[netzclub+] Your extra traffic now: 0MB
[netzclub+] You will get 300MB extra traffic in 6 days
[netzclub+] Last time extra traffic: 01-10-2019 02:00:09
[netzclub+] Last time active: 01-02-2020 13:55:48
***************************************************************************
```

### Script automatisch in zufälligen Intervallen starten (automate.py)
Die automate.py bleibt immer aktiv sobald einmal gestartet und führt das Script in zufälligen Intervallen aus.  
Alle Ausgaben des Scripts werden in die 'status.log' geschrieben so lässt sich prüfen, ob die letzte Ausführung reibungslos ablief.  
Wer keinen Cronjob/Windows Aufgabenplaner verwenden will kann die automate.py z.B. einfach beim Systemstart starten lassen.  

### FAQ
**Kann ich die [netzclub+ App](https://play.google.com/store/apps/details?id=net.netzclub.plus) und dieses Script gleichzeitig verwenden?**  
Nein. Du kannst nur eine Aktive netzclub+ Session haben d.h. wenn du dich per Script einloggst wirst du in der App ausgeloggt und andersherum ebenso.
Wenn du ausgeloggt wirst musst du zum erneuten Einloggen eine weitere Bestätigungs-SMS eingeben.
You will then have to re-enter that confirmation SMS.

**Kann ich die [normale netzclub App](https://play.google.com/store/apps/details?id=com.telefonica.netzclub.csc) und dieses Script gleichzeitig verwenden?**  
Ja.

**Wird mein netzclub Account gesperrt, wenn ich das Script verwende?**  
Garantieren kann dir das niemand, aber ein solcher Fall ist bisher nicht bekannt.

**Kann ich dieses Script mit mehreren Netzclub Accounts verwenden?**  
Nein zumindest nicht einfach so. Du kannst dir das Script in mehrere Ordner kopieren und dort jeweils andere Accounts einrichten.

**Wie kann ich dieses Script zurücksetzen??**  
Schließe das Script und lösche die Datei 'settings.json'. Bitte bedenke, dass du dann beim nächsten Start wieder eine Bestätigungs-SMS eingeben müssen wirst.


# English
Account checker for netzclub.net accounts.
Displays current used traffic and traffic available without the need to install an app or use the official website.

### Installation
1. Install Python using [this tutorial](https://gist.github.com/farOverNinethousand/2efc03be38c9932a338f1336fbef7977#python-installieren-windows)
2. Install the following Python modules using [this tutorial](https://gist.github.com/farOverNinethousand/2efc03be38c9932a338f1336fbef7977#python-module-installieren-windows):  
`` requests ``
3. Download and unzip this project.

### Usage
Run Checker.py and follow displayed instructions.
You do not necessarily have to enter your [netzclub.net](https://www.netzclub.net/login/) password but it is recommended. 
On the first run you will receive a confirmation SMS.
Be sure to run this script 2-3 times every day to make sure your account stays active.  
If everything works as expected, you should get an output like this:
```
***************************************************************************
[netzclub] Traffic left: 299MB/300MB
[netzclub+] Your extra traffic now: 0MB
[netzclub+] You will get 300MB extra traffic in 6 days
[netzclub+] Last time extra traffic: 01-10-2019 02:00:09
[netzclub+] Last time active: 01-02-2020 13:55:48
***************************************************************************
```

### FAQ
**Can I use this script and the [netzclub+ app](https://play.google.com/store/apps/details?id=net.netzclub.plus) at the same time?**  
No. If you use this script you will be automatically logged out in the netzclub+ app and the other way around.
You will then have to re-enter that confirmation SMS.

**Can I use this script and the [normal netzclub app](https://play.google.com/store/apps/details?id=com.telefonica.netzclub.csc) at the same time?**  
Yes.

**Will my account get banned if I use this script?**  
No gurantees but I don't see any reason why this should happen at this moment.

**Can I use this script with multiple netzclub accounts?**  
Not in a comfortable way but you can copy it multiple times and add different accounts for each copy ;)

**How can I reset this script?**
Close the script and delete the file 'settings.json'. Please keep in mind that you will get another Login-SMS on the first run then!