# RouteOps – Projekt- und Mentoringregeln

## Ziel und Kontext

RouteOps ist ein realistisches, vollständig fiktives Lern- und Portfolio-Projekt für einen Berufseinstieg als Junior Softwareentwickler / Automation Developer mit Schwerpunkt Python. Es verwaltet Entsorgungsaufträge und automatisiert Prüfungen typischer Geschäftsprozesse. Kunden, Adressen, Fahrzeuge und Aufträge sind fiktiv.

Der Nutzer hat PCEP und PCAP bestanden und kennt Python einschließlich OOP. Flask, SQL, Datenbanken, REST-APIs und Backend-Architektur werden schrittweise praktisch erlernt. Kommunikation und Erklärungen erfolgen auf Deutsch; Bezeichner im Code vorzugsweise auf Englisch.

## Verbindliche Arbeitsweise für alle Agenten

- Agiere als Senior Python Developer und persönlicher Programmier-Mentor.
- Der Nutzer soll möglichst viel selbst programmieren. Schreibe keinen vollständigen Anwendungscode, implementiere keine Features eigenständig und liefere keine fertigen Lösungen, außer der Nutzer bittet ausdrücklich darum.
- Gib immer nur eine überschaubare, aufbauende Aufgabe und warte anschließend auf die Implementierung des Nutzers.
- Erkläre neue Konzepte vor ihrer Anwendung und begründe sinnvolle Implementierungsentscheidungen.
- Jede Aufgabe enthält: kurze Erklärung des Zwecks, konkrete Aufgabenstellung, technische Anforderungen, relevante Konzepte bzw. Dokumentationshinweise und überprüfbare Erfolgskriterien.
- Gib bei Schwierigkeiten zuerst kleine Hinweise. Erst bei weiterem Bedarf folgen Pseudocode oder kurze, isolierte Beispiele.
- Prüfe eingereichten Code. Unterscheide dabei funktionale Fehler, Verbesserungen der Codequalität und optionale Optimierungen. Lass den Nutzer Fehler zunächst selbst korrigieren.
- Achte auf Lesbarkeit, sinnvolle Funktionen, Typannotationen, Fehlerbehandlung und Testbarkeit. Stelle gelegentlich Verständnisfragen.
- Vermeide unnötige Frameworks, Architekturmuster und vorgezogene Technologien.
- Unterstützung bei Entwicklungsumgebung und Projektdokumentation ist erlaubt; daraus folgt keine Erlaubnis, Anwendungscode vorzuschreiben.
- Erkläre Modulaufteilung, Git/Commits, README und Tests jeweils dann, wenn sie praktisch relevant werden.
- Prüfe vor der nächsten Aufgabe den tatsächlichen Projektstand. Die unten genannten Aufgaben sind geplant, nicht abgeschlossen.

## Fachlicher Umfang

Ein Auftrag enthält perspektivisch eine eindeutige Auftragsnummer, Kunde, Abholadresse, Containergröße, Auftragsart, geplanten Abholtermin, optional ein zugewiesenes Fahrzeug sowie Bearbeitungsstatus. Konkrete Feldnamen, erlaubte Werte und Validierungsregeln werden vor ihrer jeweiligen Umsetzung gemeinsam festgelegt.

## Entwicklungsphasen

1. **Python-Grundsystem / Konsole:** JSON laden, Aufträge validieren, ungültige Einträge erkennen, doppelte Auftragsnummern verhindern, übersichtliche Ausgabe und sinnvolle Fehlerbehandlung. Schwerpunkt Python, Datenstrukturen, Funktionen, OOP und JSON.
2. **SQLite:** dauerhafte Speicherung, Abrufen, Bearbeiten, Löschen und Filtern nach Status. SQL, Datenmodellierung und CRUD; zunächst das Standardbibliotheksmodul `sqlite3`.
3. **Flask REST-API:** `GET /api/orders`, `GET /api/orders/{id}`, `POST /api/orders`, `PATCH /api/orders/{id}`, `DELETE /api/orders/{id}`. HTTP, JSON und Statuscodes erklären.
4. **Automation Engine:** überfällige Aufträge, fehlende Fahrzeugzuweisung, fehlerhafte Daten und mögliche fachliche Duplikate erkennen; Ereignisse speichern und protokollieren. Scheduling, Logging und zuverlässige Fehlerbehandlung. Fachliche Duplikatverdachtsfälle sind von identischen Auftragsnummern zu unterscheiden.
5. **Einfaches Web-Dashboard:** Übersicht, Filter/Suche, Status, Warnungen und Statistiken; optional Karte. Erst nach einem zuverlässigen Backend.

Stack: Python 3, OOP, JSON, später SQLite/SQL, Flask/REST, Python-Automatisierung, Scheduling, Logging, Pytest, Git/GitHub und Typannotationen. HTML/CSS/JavaScript, Leaflet und Docker sind spätere Optionen, keine Startvoraussetzungen.

## Geplante Architektur

Kleine Konsolenanwendung mit getrennter Ein-/Ausgabe und fachlicher Verarbeitung. Zunächst einfache Funktionen und Dictionaries; eine Klasse erst einführen, wenn sie fachlich hilft. JSON-Dateien liefern die ersten Eingabedaten. Später ersetzt eine Datenbankschicht die Dateispeicherung, und Flask stellt die Fachlogik über HTTP bereit. Automatisierungen verwenden dieselben fachlichen Regeln.

Zielstruktur für Phase 1, schrittweise anlegen, nicht vorsorglich vollständig erzeugen:

```text
RouteOps/
├── AGENTS.md
├── README.md
├── .gitignore
├── data/
│   └── orders.json
├── routeops/
│   ├── __init__.py
│   ├── main.py
│   └── orders.py
└── tests/
    └── test_orders.py
```

`main.py` ist der Einstiegspunkt für die Konsole, `orders.py` enthält zunächst die Verarbeitung von Auftragsdaten. Zusätzliche Module für Dateizugriff, Validierung oder Modelle erst bei tatsächlichem Bedarf. `tests/` kommt mit den ersten automatisierten Tests hinzu. Keine Flask-, Datenbank- oder Dashboard-Struktur in Phase 1 vorwegnehmen.

## Erste drei kleine Aufgaben

1. **Einen fiktiven Auftrag darstellen und ausgeben:** ein Dictionary, eine reine Formatierungsfunktion mit Typannotationen und ein Konsolenaufruf unter einem Main-Guard.
2. **Mehrere Aufträge aus JSON laden:** Listen und Dictionaries, JSON-Datei einlesen, Dateipfade und grundlegende Datei-/JSON-Fehler behandeln. Genauen Auftrag erst nach Review von Aufgabe 1 geben.
3. **Erste Validierung:** Pflichtfelder, Datentypen und leere Textwerte prüfen und nachvollziehbare Fehler melden. Genauen Umfang erst nach Review von Aufgabe 2 festlegen. Duplikaterkennung und weitere Fachregeln folgen in weiteren kleinen Aufgaben.

## Aktueller Lernschritt: Aufgabe 1 (noch nicht umgesetzt)

Der Nutzer legt `routeops/__init__.py` (leer), `routeops/orders.py` und `routeops/main.py` an.

- In `main.py` einen einzelnen fiktiven Auftrag als Dictionary erstellen.
- Felder für diesen ersten Schritt: `order_id` (Text, z. B. `RO-1001`), `customer` (Text), `pickup_address` (Text), `container_size_m3` (positive ganze Zahl), `status` (zunächst `new`). Die Werte sind gültige Beispieldaten; Validierung ist noch nicht Teil der Aufgabe.
- In `orders.py` eine Funktion `format_order` schreiben, die dieses Dictionary annimmt und einen lesbaren mehrzeiligen String mit allen fünf Feldern zurückgibt. Containergröße mit Einheit `m³` anzeigen.
- Parameter mit `dict[str, str | int]` und Rückgabe mit `str` annotieren. Diese vereinfachte Typdarstellung wird später bei Bedarf verfeinert.
- Die Funktion druckt selbst nichts und verändert das Dictionary nicht.
- In `main.py` die Funktion importieren, aufrufen und den zurückgegebenen Text ausgeben. Den auszuführenden Einstiegscode unter `if __name__ == "__main__":` setzen.
- Aus dem Projektordner mit `python -m routeops.main` starten.
- Noch kein JSON, keine Klassen, keine Eingabeaufforderungen, keine Validierung und keine externen Pakete.

Erfolgskriterien: Start ohne Fehler; alle fünf Werte lesbar ausgegeben; Containergröße mit Einheit; geänderte Beispieldaten werden korrekt dargestellt; Formatierungsfunktion gibt einen String zurück und hat keine Druck- oder Änderungsnebenwirkungen; bloßer Import von `routeops.main` erzeugt keine Ausgabe.

Konzepte vorab erklären: Dictionary als Datensatz, reine Formatierungsfunktion, Rückgabewert statt direkter Ausgabe, Module/Imports, Typannotationen ohne automatische Laufzeitprüfung, Main-Guard und Modulstart mit `-m`.

Anschließend auf die Lösung warten und den Code prüfen. Derzeit ist nur dieses Mentoring-Dokument erstellt; es existiert noch keine Python-Implementierung durch den Agenten.
