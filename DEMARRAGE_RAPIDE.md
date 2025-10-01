# 🚀 AtHome - Guide de Démarrage Rapide

## ✨ Nouvelles Interfaces Modernes

### 📋 Ce qui a été développé

#### 1. **Interface Video Streamer Moderne** (`launch_streamer.py`)
✅ **Interface complète avec:**
- 📹 Gestion caméras USB avec détection automatique
- 🌐 Ajout de caméras IP (RTSP) avec formulaire dédié
- ⚙️ Paramètres avancés: résolution (640p à 4K), FPS (15-60), codec (h264, h265, vp8, vp9, mjpeg)
- 🔄 Rotation (0°, 90°, 180°, 270°) et miroirs H/V
- 🌐 Streaming web avec URL réseau local
- ⏺️ Enregistrement avec choix format (AVI, MP4, MKV, MOV) et dossier personnalisé
- 📱 QR Code pour appairage rapide
- 📷 Prévisualisation en direct avec contrôles

#### 2. **Interface Camera Viewer Moderne** (`launch_viewer.py`)
✅ **Visualisation multi-caméras avec:**
- 🔢 **Grilles personnalisables**: 1, 2, 3, 4, 6, ou 9 caméras simultanées
- 🔊 **Audio par caméra**: Contrôle micro individuel pour chaque flux
- ⛶ Mode plein écran par caméra
- 📷 Capture snapshot individuelle ou globale
- ⏺️ Enregistrement multi-caméras avec audio
- 🎛️ Contrôles avancés: qualité, ratio d'aspect, synchronisation A/V
- 📱 Scanner QR pour connexion rapide
- 🔄 Reconnexion automatique

#### 3. **Système d'Installation** (`setup_installer.py`)
✅ **Installeur universel qui:**
- Vérifie Python 3.8+
- Installe dépendances automatiquement
- Crée configuration par défaut
- Crée répertoires (recordings, snapshots, logs)
- Génère raccourcis bureau (Windows/Linux/macOS)
- Exécute tests de validation

---

## 🎯 Comment Utiliser

### Installation

```bash
# Sur votre machine locale (avec Python 3.8+)
python setup_installer.py
```

### Lancement des Interfaces

#### Streamer (Diffusion vidéo)
```bash
python launch_streamer.py
```

**Étapes:**
1. L'interface moderne s'ouvre
2. Onglet "📹 Caméras": Sélectionner USB ou cliquer "➕ Ajouter IP"
3. Onglet "⚙️ Paramètres": Configurer résolution, FPS, codec
4. Onglet "🌐 Streaming Web": Activer et copier URL
5. Onglet "⏺ Enregistrement": Choisir dossier et format
6. Cliquer "▶ Démarrer" pour lancer
7. Scanner QR code depuis l'onglet "📱 QR Code"

#### Viewer (Visualisation)
```bash
python launch_viewer.py
```

**Étapes:**
1. L'interface moderne s'ouvre
2. Choisir disposition (1, 2, 3, 4, 6, ou 9 caméras) en haut
3. Onglet "📹 Caméras": Cliquer "📱 Scanner QR" ou "➕ Ajouter"
4. Onglet "🖥️ Affichage": Configurer qualité et ratio
5. Onglet "🔊 Audio": Activer audio principal et par caméra
6. Onglet "⏺ Enregistrement": Options enregistrement multi-cam
7. Connecter aux caméras avec "🔌 Connecter"

---

## 📐 Layouts Disponibles (Viewer)

### 1 Caméra - Plein Écran
```
┌─────────────────┐
│                 │
│     Caméra 1    │
│                 │
└─────────────────┘
```

### 2 Caméras - Côte à côte
```
┌────────┬────────┐
│ Cam 1  │ Cam 2  │
└────────┴────────┘
```

### 3 Caméras - 1 grande + 2 petites
```
┌────────┬────────┐
│        │ Cam 2  │
│ Cam 1  ├────────┤
│        │ Cam 3  │
└────────┴────────┘
```

### 4 Caméras - Grille 2×2
```
┌────────┬────────┐
│ Cam 1  │ Cam 2  │
├────────┼────────┤
│ Cam 3  │ Cam 4  │
└────────┴────────┘
```

### 6 Caméras - Grille 2×3
```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
└───┴───┴───┘
```

### 9 Caméras - Grille 3×3
```
┌──┬──┬──┐
│1 │2 │3 │
├──┼──┼──┤
│4 │5 │6 │
├──┼──┼──┤
│7 │8 │9 │
└──┴──┴──┘
```

---

## 🎬 Fonctionnalités Principales

### Streamer
- ✅ Détection auto caméras USB
- ✅ Caméras IP (RTSP): `rtsp://user:pass@ip:port/stream`
- ✅ Résolutions: 640×480 à 3840×2160 (4K)
- ✅ FPS: 15, 24, 30, 60
- ✅ Codecs: H.264, H.265, VP8, VP9, MJPEG
- ✅ Rotation: 0°, 90°, 180°, 270°
- ✅ Miroirs horizontal/vertical
- ✅ Qualité ajustable: 10-100%
- ✅ Streaming web local
- ✅ Enregistrement AVI/MP4/MKV/MOV
- ✅ QR code appairage

### Viewer
- ✅ Affichage 1-9 caméras
- ✅ Audio par caméra (🔊/🔇)
- ✅ Plein écran individuel (⛶)
- ✅ Capture snapshot (📷)
- ✅ Enregistrement multi-cam (⏺)
- ✅ Qualité: Basse, Moyenne, Haute, Ultra
- ✅ Ratio: 4:3, 16:9, 16:10, 21:9
- ✅ Mode: Adapté, Étiré, Recadré, Original
- ✅ Reconnexion auto
- ✅ Affichage FPS/timestamp
- ✅ Volume global ajustable

---

## ⚙️ Configuration Caméra IP

### Format URL RTSP
```
rtsp://[utilisateur]:[motdepasse]@[ip]:[port]/[chemin]
```

### Exemples
```bash
# Hikvision
rtsp://admin:12345@192.168.1.100:554/Streaming/Channels/101

# Dahua
rtsp://admin:admin@192.168.1.101:554/cam/realmonitor?channel=1&subtype=0

# Generic RTSP
rtsp://192.168.1.102/live/main

# ONVIF
rtsp://admin:pass@192.168.1.103:8554/profile1
```

---

## 🔧 Paramètres Recommandés

### Usage Résidentiel
```
Résolution: 1280×720 (HD)
FPS: 30
Codec: h264
Qualité: 80%
Format enregistrement: MP4
```

### Surveillance Professionnelle
```
Résolution: 1920×1080 (Full HD)
FPS: 30
Codec: h265 (meilleure compression)
Qualité: 90%
Format enregistrement: MKV
```

### Basse Bande Passante
```
Résolution: 640×480
FPS: 15
Codec: h264
Qualité: 50%
Format enregistrement: AVI
```

---

## 📁 Structure des Fichiers

```
AtHome/
├── recordings/              # Vidéos enregistrées
├── snapshots/              # Captures d'écran
├── logs/                   # Fichiers log
├── athome_config.json     # Configuration
└── README.md              # Documentation complète
```

---

## 🐛 Dépannage

### Caméra USB non détectée
1. Vérifier connexion physique
2. Actualiser la liste (🔄 Actualiser)
3. Tester avec autre application
4. Vérifier permissions (Linux: `/dev/video*`)

### Caméra IP ne se connecte pas
1. Vérifier URL RTSP (ping IP)
2. Tester credentials
3. Vérifier port (554 standard)
4. Firewall désactivé

### Audio ne fonctionne pas
1. Activer "Audio principal" dans Viewer
2. Cliquer 🔊 sur caméra spécifique
3. Vérifier volume global
4. Tester sortie audio système

### Enregistrement échoue
1. Vérifier espace disque
2. Permissions dossier d'enregistrement
3. Format supporté (MP4 recommandé)
4. Codec compatible

---

## 🔐 Sécurité

⚠️ **À implémenter (prochaines étapes):**
- [ ] Authentification signaling server
- [ ] Mot de passe streaming web
- [ ] Chiffrement QR code
- [ ] HTTPS/TLS
- [ ] Tokens session

---

## 📊 État d'Implémentation

### ✅ Complété
- Interface moderne Streamer (UI)
- Interface moderne Viewer (UI)
- Grilles multi-caméras
- Contrôles audio UI
- Options enregistrement UI
- Launchers & installeur
- Documentation

### 🔧 Intégration Nécessaire
- Pipeline WebRTC dans UI
- Capture/lecture audio réelle
- Enregistrement effectif
- Ouverture flux RTSP
- Appairage QR fonctionnel
- URL streaming local

### 🔮 Fonctionnalités Futures
- Viewer navigateur web
- Cloud storage (S3, FTP)
- Notifications actives
- Application mobile
- IA détection objets

---

## 💡 Conseils d'Utilisation

1. **Multi-caméras**: Commencer avec layout 4 caméras pour tester
2. **Audio**: Activer une caméra audio à la fois pour éviter interférences
3. **Enregistrement**: Format MP4 + H.264 = meilleure compatibilité
4. **Réseau local**: Partager URL streaming pour accès autres appareils
5. **QR Code**: Scanner avec smartphone pour appairage rapide

---

## 📞 Support

- Documentation complète: `README.md`
- Configuration projet: `replit.md`
- Tests: `python test_athome.py`

---

**Développé avec ❤️ - Interface moderne pour vidéosurveillance intelligente**
