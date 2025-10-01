# 🎥 AtHome Video Surveillance System

## Système de Vidéosurveillance Moderne avec Interface Avancée

### 🌟 Nouvelles Fonctionnalités

#### AtHome Video Streamer - Interface Moderne
- ✅ Design moderne avec thème sombre professionnel
- ✅ Support complet caméras **USB et IP (RTSP)**
- ✅ Détection automatique des caméras connectées au PC
- ✅ Streaming web avec URL réseau local pour accès internet
- ✅ Paramètres avancés: résolution, FPS, codec, qualité, rotation, miroirs
- ✅ Enregistrement en direct avec choix de format (AVI, MP4, MKV, MOV)
- ✅ Choix du dossier d'enregistrement personnalisé
- ✅ QR code pour appairage rapide
- ✅ Prévisualisation en direct avec overlay

#### AtHome Camera Viewer - Interface Moderne
- ✅ Affichage multi-caméras avec **grilles personnalisables**
- ✅ Layouts disponibles: **1, 2, 3, 4, 6, 9 caméras**
- ✅ **Support audio/micro en direct** pour chaque caméra
- ✅ Contrôles individuels par caméra (audio, plein écran, capture)
- ✅ Paramètres d'affichage avancés (qualité, ratio, mode)
- ✅ Enregistrement multi-caméras simultané avec audio
- ✅ Gestion complète de l'audio (volume, sortie, synchronisation)
- ✅ Scanner QR pour connexion rapide
- ✅ Reconnexion automatique

---

## 📁 Structure du Projet

```
AtHome/
├── 📹 VIDEO STREAMER/
│   ├── modern_streamer_gui.py     # Interface moderne streamer
│   ├── camera_capture.py          # Capture USB/IP
│   └── webrtc_sender.py           # Transmission WebRTC
│
├── 🖥️ CAMERA VIEWER/
│   ├── modern_viewer_gui.py       # Interface moderne viewer
│   └── webrtc_receiver.py         # Réception WebRTC
│
├── 🔐 SÉCURITÉ & CONFIG/
│   └── athome_config.py           # Configuration
│
├── 🔍 DÉTECTION & ANALYSE/
│   ├── motion_detector.py         # Détection mouvement
│   └── zone_editor.py             # Zones personnalisées
│
├── 💾 STOCKAGE/
│   └── storage_manager.py         # Gestion enregistrements
│
├── 📢 NOTIFICATIONS/
│   └── notification_manager.py    # Alertes Email/Telegram
│
├── 🌐 SERVEUR DE SIGNALISATION/
│   └── signaling_server.py        # WebRTC signaling
│
├── 🌐 INTERFACE WEB/
│   └── web_server.py              # Interface web
│
├── launch_streamer.py             # 🚀 Lancer Video Streamer
├── launch_viewer.py               # 🚀 Lancer Camera Viewer
├── setup_installer.py             # 📦 Installeur complet
└── requirements.txt               # Dépendances Python
```

---

## 🚀 Installation Rapide

### Option 1: Installation Automatique

```bash
python setup_installer.py
```

L'installeur va:
- ✅ Vérifier Python (3.8+ requis)
- ✅ Installer toutes les dépendances
- ✅ Créer la configuration par défaut
- ✅ Créer les répertoires nécessaires
- ✅ Créer les raccourcis bureau (Windows/Linux)
- ✅ Exécuter les tests de validation

### Option 2: Installation Manuelle

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Lancer le serveur de signalisation
python "🌐 SERVEUR DE SIGNALISATION/signaling_server.py"

# 3. Lancer le Video Streamer
python launch_streamer.py

# 4. Lancer le Camera Viewer
python launch_viewer.py
```

---

## 📖 Guide d'Utilisation

### 1️⃣ Video Streamer (Diffusion)

```bash
python launch_streamer.py
```

**Configuration Caméra:**
- 📹 **Caméras USB**: Détection automatique, sélection dans la liste
- 🌐 **Caméras IP**: Cliquer "➕ Ajouter IP", entrer URL RTSP
- ⚙️ **Paramètres**: Résolution, FPS, codec, rotation, miroirs
- 🌐 **Streaming Web**: Activer pour accès réseau local
- ⏺ **Enregistrement**: Choisir format, qualité, dossier

**Workflow:**
1. Sélectionner une caméra USB ou ajouter caméra IP
2. Configurer les paramètres (résolution, FPS, etc.)
3. Cliquer "▶ Démarrer" pour lancer le streaming
4. Scanner le QR code avec le viewer pour se connecter
5. Activer "⏺ Enregistrer" pour capturer la vidéo

### 2️⃣ Camera Viewer (Visualisation)

```bash
python launch_viewer.py
```

**Affichage Multi-Caméras:**
- 🔢 **Choisir disposition**: 1, 2, 3, 4, 6 ou 9 caméras
- ➕ **Ajouter caméras**: Scanner QR ou ajouter manuellement
- 🔊 **Audio**: Activer micro pour chaque caméra individuellement
- 📷 **Capture**: Prendre snapshot d'une ou toutes les caméras
- ⏺ **Enregistrement**: Enregistrer une ou toutes les caméras

**Contrôles par Caméra:**
- 🔊/🔇 : Activer/désactiver audio
- ⛶ : Mode plein écran
- 📷 : Capture snapshot

**Layouts Disponibles:**
- **1 caméra**: Plein écran
- **2 caméras**: Vue côte à côte
- **3 caméras**: 1 grande + 2 petites
- **4 caméras**: Grille 2×2
- **6 caméras**: Grille 2×3
- **9 caméras**: Grille 3×3

### 3️⃣ Configuration Avancée

#### Caméras IP (RTSP)
```python
# Format URL RTSP
rtsp://username:password@ip:port/stream

# Exemples:
rtsp://admin:123456@192.168.1.100:554/stream1
rtsp://192.168.1.101/live/main
```

#### Streaming Web
- Active le serveur HTTP pour accès navigateur
- URL: `http://[IP_LOCAL]:[PORT]/stream`
- Authentification optionnelle
- Copier l'URL pour partager

#### Audio Direct
- Active le micro de chaque caméra individuellement
- Volume global ajustable
- Synchronisation audio/vidéo automatique
- Sortie configurable (haut-parleurs, casque)

---

## 🛠️ Technologies Utilisées

- **Python 3.11** - Langage principal
- **Tkinter** - Interface graphique moderne
- **OpenCV** - Traitement vidéo et détection
- **WebRTC (aiortc)** - Streaming P2P
- **aiohttp** - Serveur web asynchrone
- **WebSockets** - Signalisation temps réel
- **NumPy** - Traitement numérique
- **Pillow** - Manipulation d'images
- **QRCode** - Génération QR codes

---

## 📋 Fonctionnalités Complètes

### Video Streamer
- ✅ Détection automatique caméras USB
- ✅ Support caméras IP (RTSP, HTTP)
- ✅ Configuration avancée (résolution, FPS, codec)
- ✅ Rotation et miroirs (H/V)
- ✅ Qualité ajustable (10-100%)
- ✅ Streaming WebRTC P2P
- ✅ Streaming web HTTP
- ✅ Enregistrement multi-format
- ✅ Choix dossier enregistrement
- ✅ Enregistrement sur mouvement
- ✅ QR code appairage
- ✅ Prévisualisation temps réel

### Camera Viewer
- ✅ Affichage 1-9 caméras simultanées
- ✅ Grilles personnalisables (1, 2, 3, 4, 6, 9)
- ✅ Audio micro en direct par caméra
- ✅ Contrôles individuels par vue
- ✅ Mode plein écran par caméra
- ✅ Capture snapshot individuelle/globale
- ✅ Enregistrement multi-caméras
- ✅ Qualité d'affichage ajustable
- ✅ Ratios d'aspect configurables
- ✅ Reconnexion automatique
- ✅ Affichage FPS/timestamp
- ✅ Volume audio global
- ✅ Synchronisation A/V

### Système Global
- ✅ Détection de mouvement
- ✅ Zones de détection personnalisées
- ✅ Stockage local avec rétention
- ✅ Notifications Email/Telegram
- ✅ Serveur signalisation WebRTC
- ✅ Interface web moderne
- ✅ Configuration JSON
- ✅ Tests d'intégration

---

## 🎯 Cas d'Usage

### 🏠 Maison
- Surveillance entrée, jardin, garage
- Monitoring bébé avec audio
- Sécurité périmètre

### 🏢 Bureau
- Surveillance espaces communs
- Monitoring salles serveurs
- Sécurité parking

### 🏭 Industriel
- Surveillance chaînes production
- Monitoring zones sensibles
- Contrôle qualité visuel

### 🛍️ Commerce
- Surveillance magasin multi-angles
- Monitoring caisses
- Analyse comportement client

---

## 🔧 Configuration

### Fichier `athome_config.json`

```json
{
    "camera": {
        "resolution": [1920, 1080],
        "fps": 30,
        "codec": "h264"
    },
    "detection": {
        "enabled": true,
        "sensitivity": 50
    },
    "storage": {
        "local_path": "./recordings",
        "retention_days": 30
    }
}
```

---

## 📊 Tests

```bash
# Lancer tous les tests
python test_athome.py

# Tests inclus:
# ✅ Structure fichiers
# ✅ Dépendances
# ✅ Imports modules
# ✅ Configuration
# ✅ Détection caméras
# ✅ Serveur signalisation
```

---

## 🌐 Accès Web

L'interface web est accessible à:
- **Local**: http://localhost:5000
- **Réseau**: http://[IP_LOCAL]:5000

Elle affiche:
- État du système
- Fonctionnalités actives
- Documentation
- Technologies utilisées

---

## 🐛 Dépannage

### Caméra non détectée
- Vérifier connexion USB
- Tester avec autre logiciel
- Vérifier permissions caméra

### Pas de vidéo
- Vérifier serveur signalisation (port 8080)
- Tester connexion réseau
- Vérifier firewall

### Audio ne fonctionne pas
- Activer audio dans paramètres
- Vérifier micro caméra
- Tester sortie audio système

### Enregistrement échoue
- Vérifier espace disque
- Permissions dossier
- Codec supporté par système

---

## 📝 Licence

Projet AtHome Video Surveillance System
© 2025 - Système de vidéosurveillance open source

---

## 👥 Support

Pour toute question ou problème:
1. Consulter la documentation
2. Vérifier les tests
3. Examiner les logs
4. Contacter le support

---

**Développé avec ❤️ pour une surveillance intelligente et accessible**
