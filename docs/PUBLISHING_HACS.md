# HACS Publishing Workflow - Vollständige Anleitung

Komplette Schritt-für-Schritt Anleitung zur Veröffentlichung der BAUERGROUP Hargassner Integration in HACS Default Repositories.

## 📋 Voraussetzungen

### ✅ Was bereits vorhanden ist:
- [x] Repository auf GitHub
- [x] Korrekte Verzeichnisstruktur
- [x] `manifest.json` mit allen erforderlichen Feldern
- [x] `hacs.json` Konfiguration
- [x] GitHub Workflows (HACS, Hassfest, Release)
- [x] Umfassende Dokumentation
- [x] README.md

### ❌ Was noch benötigt wird:
- [ ] Home Assistant Brands Eintrag
- [ ] GitHub Release erstellen
- [ ] HACS Pull Request

---

## 🚀 Phase 1: Home Assistant Brands Registration

### Schritt 1: Fork home-assistant/brands

1. Gehe zu: https://github.com/home-assistant/brands
2. Klicke auf "Fork" (oben rechts)
3. Erstelle Fork in deinem Account

### Schritt 2: Clone deinen Fork

```bash
git clone https://github.com/YOUR_USERNAME/brands.git
cd brands
```

### Schritt 3: Erstelle Integration Verzeichnis

```bash
mkdir -p custom_integrations/bauergroup_hargassnerintegration
cd custom_integrations/bauergroup_hargassnerintegration
```

### Schritt 4: Icon vorbereiten

**Anforderungen:**
- Format: PNG
- Größe: 256x256 oder 512x512 Pixel
- Transparenter Hintergrund empfohlen
- Dateiname: `icon.png`

```bash
# Kopiere dein Icon
cp /path/to/your/icon.png icon.png
```

### Schritt 5: Logo vorbereiten (optional)

```bash
# Falls vorhanden, hochauflösendes Logo
cp /path/to/your/logo.png logo.png
```

### Schritt 6: manifest.json erstellen

Erstelle `manifest.json`:

```json
{
  "domain": "bauergroup_hargassnerintegration",
  "name": "BAUERGROUP Hargassner Integration",
  "integration_type": "device",
  "iot_class": "local_polling"
}
```

### Schritt 7: Brands PR erstellen

```bash
git checkout -b add-bauergroup-hargassner
git add custom_integrations/bauergroup_hargassnerintegration/
git commit -m "Add BAUERGROUP Hargassner Integration"
git push origin add-bauergroup-hargassner
```

Erstelle Pull Request auf GitHub:
- Base: `home-assistant/brands:main`
- Head: `YOUR_USERNAME/brands:add-bauergroup-hargassner`
- Titel: "Add BAUERGROUP Hargassner Integration"

**⏳ Warten auf Merge** (kann einige Tage dauern)

---

## 🔍 Phase 2: GitHub Workflows testen

### Schritt 1: Workflows aktivieren

Nach dem nächsten Push werden die Workflows automatisch ausgeführt.

```bash
cd /path/to/BAUERGROUP.Internal.Integration.Hargassner
git add .github/workflows/
git commit -m "feat: Add HACS and Hassfest workflows"
git push origin main
```

### Schritt 2: Workflow-Status prüfen

1. Gehe zu: https://github.com/bauer-group/BAUERGROUP.Internal.Integration.Hargassner/actions
2. Prüfe Status von:
   - ✅ **HACS Validation** - muss grün sein
   - ✅ **Hassfest** - muss grün sein

### Schritt 3: Fehler beheben (falls vorhanden)

**Häufige Fehler:**

#### HACS Validation Fehler:
```
Error: hacs.json validation failed
```
**Lösung:** Prüfe `hacs.json` auf korrekte Syntax

#### Hassfest Fehler:
```
Error: manifest.json missing required field
```
**Lösung:** Prüfe `manifest.json` Pflichtfelder

**Wiederhole Push bis alle Workflows grün sind!**

---

## 📦 Phase 3: GitHub Release erstellen

### Schritt 1: Version finalisieren

Stelle sicher dass:
- Alle Tests grün sind ✅
- CHANGELOG.md aktualisiert ist
- README.md vollständig ist
- Dokumentation aktuell ist

### Schritt 2: Git Tag erstellen

```bash
# Aktuellen Stand committen
git add .
git commit -m "chore: Prepare release v0.1.0"
git push origin main

# Tag erstellen
git tag -a v0.1.0 -m "Release v0.1.0 - Initial HACS release

✨ Added
- Thread-safe Telnet Client with auto-reconnect
- Config Flow for GUI-based configuration
- 16 standard sensors + full mode
- Energy Dashboard integration
- Bilingual support (EN/DE)
- Comprehensive documentation

See CHANGELOG.md for full details"

# Tag pushen
git push origin v0.1.0
```

### Schritt 3: GitHub Release erstellen

1. Gehe zu: https://github.com/bauer-group/BAUERGROUP.Internal.Integration.Hargassner/releases
2. Klicke "Draft a new release"
3. Wähle Tag: `v0.1.0`
4. Release title: `v0.1.0 - Initial HACS Release`
5. Description:

```markdown
## 🎉 Initial HACS Release

Dies ist die erste offizielle Release der BAUERGROUP Hargassner Integration für Home Assistant.

### ✨ Features

- **Thread-safe Telnet Client** mit automatischer Reconnect-Funktion
- **Config Flow** für GUI-basierte Konfiguration
- **16 Standard-Sensoren** + FULL-Modus mit allen Parametern
- **Energy Dashboard** Integration (Wärmemenge-Sensor)
- **Zweisprachig** (Deutsch/Englisch)
- **Umfassende Dokumentation**

### 📊 Supported Firmware

- V14_1HAR_q1 (vollständig getestet)

### 📚 Documentation

- [Installation Guide](https://github.com/bauer-group/BAUERGROUP.Internal.Integration.Hargassner/blob/main/docs/INSTALLATION.md)
- [Architecture Documentation](https://github.com/bauer-group/BAUERGROUP.Internal.Integration.Hargassner/blob/main/docs/ARCHITECTURE.md)
- [Development Guide](https://github.com/bauer-group/BAUERGROUP.Internal.Integration.Hargassner/blob/main/docs/DEVELOPMENT.md)

### 🔧 Installation

Via HACS (nach Aufnahme ins Default Repository):
1. HACS → Integrations
2. Search "Hargassner"
3. Install

Manuelle Installation:
1. Download `bauergroup_hargassnerintegration.zip`
2. Extract to `custom_components/`
3. Restart Home Assistant

See [INSTALLATION.md](https://github.com/bauer-group/BAUERGROUP.Internal.Integration.Hargassner/blob/main/docs/INSTALLATION.md) for details.

---

**Full Changelog**: https://github.com/bauer-group/BAUERGROUP.Internal.Integration.Hargassner/blob/main/CHANGELOG.md
```

6. **WICHTIG:** Prüfe "Set as the latest release"
7. Klicke "Publish release"

### Schritt 4: Release Workflow prüfen

Nach dem Publish sollte der `Release` Workflow automatisch laufen:
- Gehe zu Actions Tab
- Prüfe dass "Release" Workflow erfolgreich ist ✅

---

## 🎯 Phase 4: HACS Pull Request

### Schritt 1: HACS Default Repository forken

1. Gehe zu: https://github.com/hacs/default
2. Klicke "Fork"
3. Clone deinen Fork:

```bash
git clone https://github.com/YOUR_USERNAME/default.git hacs-default
cd hacs-default
```

### Schritt 2: Branch erstellen

```bash
git checkout -b add-bauergroup-hargassner
```

### Schritt 3: Integration hinzufügen

Editiere die Datei `integration`:

```bash
# Öffne Editor
nano integration

# ODER
code integration
```

**Füge ALPHABETISCH SORTIERT hinzu:**

```
bauer-group/BAUERGROUP.Internal.Integration.Hargassner
```

**WICHTIG:**
- Exakt der GitHub Repository Pfad
- Alphabetisch zwischen anderen Einträgen
- NICHT am Ende anfügen!

### Schritt 4: Commit und Push

```bash
git add integration
git commit -m "Add BAUERGROUP Hargassner Integration"
git push origin add-bauergroup-hargassner
```

### Schritt 5: Pull Request erstellen

1. Gehe zu: https://github.com/hacs/default
2. Klicke "New Pull Request"
3. Click "compare across forks"
4. Base: `hacs/default:master`
5. Head: `YOUR_USERNAME/default:add-bauergroup-hargassner`

**PR Template ausfüllen:**

```markdown
## Repository URL
https://github.com/bauer-group/BAUERGROUP.Internal.Integration.Hargassner

## Category
integration

## Description
BAUERGROUP Hargassner Integration provides integration for Hargassner pellet boilers with Home Assistant via Telnet protocol.

## Features
- Thread-safe Telnet client with automatic reconnection
- GUI-based configuration (Config Flow)
- 16 standard sensors + full mode with all firmware parameters
- Energy Dashboard integration
- Bilingual support (English/German)
- Multi-firmware support

## Checklist
- [x] Repository is public
- [x] HACS validation passes
- [x] Hassfest validation passes
- [x] GitHub release created
- [x] Home Assistant Brands submitted
- [x] Repository follows HACS requirements
- [x] `hacs.json` present and valid
- [x] `manifest.json` present and valid
- [x] README.md with installation instructions
- [x] Only one integration per repository
- [x] All files in `custom_components/bauergroup_hargassnerintegration/`

## Additional Information
- First release: v0.1.0
- Supported firmware: V14_1HAR_q1
- Tested with Home Assistant 2024.1+
```

6. Klicke "Create Pull Request"

### Schritt 6: Warten auf Review

**Timeline:**
- ⏳ Review kann mehrere Wochen bis Monate dauern
- 🔔 Sei bereit auf Feedback zu reagieren
- ✅ Nach Merge: Integration erscheint im nächsten HACS Scan

---

## 📝 Phase 5: Nach der Aufnahme

### Nach HACS Merge

1. **Ankündigung:**
   - Forum Post im Home Assistant Community Forum
   - GitHub Diskussion starten
   - Social Media (falls gewünscht)

2. **Monitoring:**
   - GitHub Issues im Auge behalten
   - Auf User-Feedback reagieren
   - Bug-Reports zeitnah bearbeiten

3. **Updates:**
   - Regelmäßige Updates mit neuen Features
   - Firmware-Versionen hinzufügen
   - Sicherheits-Updates

### Release-Prozess für Updates

```bash
# 1. Änderungen committen
git add .
git commit -m "feat: Add new feature XYZ"
git push origin main

# 2. CHANGELOG.md aktualisieren
# (Version und Änderungen eintragen)

# 3. Tag erstellen
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin v0.2.0

# 4. GitHub Release erstellen
# (wie in Phase 3)
```

HACS erkennt neue Releases automatisch und zeigt sie Usern an!

---

## 🆘 Troubleshooting

### HACS Validation schlägt fehl

**Problem:** `hacs.json` validation error

**Lösung:**
```bash
# Prüfe hacs.json Syntax
cat hacs.json | python -m json.tool

# Häufige Fehler:
# - Fehlendes Komma
# - Falsche Anführungszeichen
# - Fehlende Felder
```

### Hassfest schlägt fehl

**Problem:** `manifest.json` validation error

**Lösung:**
```bash
# Prüfe erforderliche Felder:
# - domain
# - name
# - version
# - codeowners
# - documentation
# - issue_tracker
```

### Brands PR wird abgelehnt

**Mögliche Gründe:**
- Icon falsche Größe (muss 256x256 oder 512x512 sein)
- Manifest.json unvollständig
- Domain stimmt nicht überein

### HACS PR wird abgelehnt

**Mögliche Gründe:**
- Workflows nicht grün
- Brands noch nicht merged
- Kein Release vorhanden
- Nicht alphabetisch sortiert

---

## 📚 Ressourcen

- [HACS Documentation](https://hacs.xyz/docs/publish/include/)
- [Home Assistant Brands](https://github.com/home-assistant/brands)
- [Integration Development](https://developers.home-assistant.io/)
- [HACS Discord](https://discord.gg/apgchf8)

---

## ✅ Checkliste für Publishing

Nutze diese Checkliste um sicherzustellen, dass alles erledigt ist:

### Vorbereitung
- [ ] Alle Tests grün (lokal und CI)
- [ ] Dokumentation vollständig
- [ ] README.md mit Screenshots
- [ ] CHANGELOG.md aktualisiert
- [ ] Code reviewed

### GitHub Workflows
- [ ] `.github/workflows/hacs.yml` erstellt
- [ ] `.github/workflows/hassfest.yml` erstellt
- [ ] `.github/workflows/release.yml` erstellt
- [ ] Alle Workflows laufen erfolgreich

### Home Assistant Brands
- [ ] Fork erstellt
- [ ] Icon (256x256 oder 512x512 PNG) hinzugefügt
- [ ] manifest.json erstellt
- [ ] Pull Request erstellt
- [ ] PR merged

### GitHub Release
- [ ] Git Tag erstellt
- [ ] Release auf GitHub published
- [ ] Release Notes vollständig
- [ ] Assets angehängt (falls vorhanden)

### HACS Submission
- [ ] hacs/default Fork erstellt
- [ ] Integration alphabetisch in `integration` Datei eingefügt
- [ ] Pull Request erstellt mit vollständigem Template
- [ ] Auf Review reagiert
- [ ] PR merged

### Nach Veröffentlichung
- [ ] Ankündigung im Forum
- [ ] Issues überwachen
- [ ] Dokumentation auf dem neuesten Stand
- [ ] Regelmäßige Updates planen

---

**Viel Erfolg bei der Veröffentlichung! 🚀**

Bei Fragen: [GitHub Discussions](https://github.com/bauer-group/BAUERGROUP.Internal.Integration.Hargassner/discussions)
