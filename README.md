# ⚠️ TCP SYN Flood Simulation Script (Scapy)

> **Ce script est strictement à but pédagogique et ne doit être utilisé que dans un environnement de test isolé.**
> Il permet de simuler un envoi de paquets TCP SYN avec des adresses IP et MAC falsifiées, à des fins d’analyse réseau locale.

---

## ❗ AVERTISSEMENT IMPORTANT

### 🚨 Interdiction d’usage sur des réseaux publics

Ce script envoie de **faux paquets TCP SYN** (spoofing IP + MAC) à une destination IP. Il **peut être interprété comme une tentative de DDoS** s’il est utilisé sur Internet ou vers des serveurs réels.

⚠️ **Son exécution en dehors d’un environnement local (lab, VM, réseau isolé) constitue une violation éthique et légale.**

L’auteur de ce dépôt **décline toute responsabilité** en cas de mauvaise utilisation.

---

## 🎯 Objectif pédagogique

- Comprendre comment un SYN Flood fonctionne (attaque par envoi massif de paquets SYN)
- Apprendre à générer des paquets TCP personnalisés avec [Scapy](https://scapy.net/)
- Observer le comportement réseau dans un lab local via Wireshark ou autres outils

---

## 📦 Dépendances

- Python 3.x
- [Scapy](https://scapy.readthedocs.io/)

```bash
pip install scapy
