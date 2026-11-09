# SAE5.02-Centralisation-VoIP
Projet SAÉ 5.02 - Centralisation des informations clients et maquette VoIP Asterisk

## Présentation du projet

Ce projet part d’un besoin rencontré en entreprise. Les informations techniques des clients sont aujourd’hui réparties dans plusieurs fichiers Excel. Lorsqu’un technicien doit traiter un incident, il peut donc perdre du temps à rechercher les bonnes informations sur le client, son site ou son installation téléphonique.

L’objectif du projet est de créer une application web simple qui centralise ces informations dans une base de données. Le technicien pourra rechercher un client par son nom, son adresse mail ou son domaine, consulter ses informations techniques et créer un ticket directement à partir de sa fiche.

## Partie application

L’application sera développée avec Python et Flask. Les données seront stockées dans une base MariaDB.

La base contiendra principalement les clients, leurs différents sites, leurs informations techniques et les tickets créés par les techniciens.

L’application permettra au minimum de rechercher un client, afficher ses informations techniques et créer un ticket lié au bon client et au bon site.

## Partie VoIP

Une maquette VoIP sera également mise en place afin de reproduire quelques situations simples rencontrées dans le domaine de la téléphonie.

Deux instances Asterisk seront utilisées. La première représentera le système téléphonique d’un client et la seconde simulera un opérateur SIP.

Des postes SIP de test, par exemple les extensions 101 et 102, permettront de tester les appels internes. Un trunk SIP entre les deux serveurs Asterisk permettra également de simuler des appels entrants et sortants.

Cette maquette servira ensuite à tester quelques incidents simples, par exemple un trunk indisponible ou un poste SIP non enregistré.

## Architecture prévue

Le projet utilisera trois machines virtuelles.

La première VM sera la machine **Manager**. Elle contiendra Ansible et Git et servira à automatiser le déploiement des autres machines.

La deuxième VM sera la machine **Application**. Elle hébergera Docker, l’application Flask et la base MariaDB.

La troisième VM sera la machine **VoIP**. Elle hébergera les deux instances Asterisk utilisées pour le laboratoire téléphonique.

L’adressage prévu est le suivant :

- VM Manager : `192.168.50.10`
- VM Application : `192.168.50.20`
- VM VoIP : `192.168.50.30`

## Automatisation avec Ansible

Le déploiement du projet sera progressivement automatisé avec Ansible.

Un playbook principal `site.yml` sera utilisé pour préparer les machines, installer Docker, déployer l’application, créer la base MariaDB, configurer Asterisk et appliquer les règles de pare-feu nécessaires.

Les rôles prévus sont :

`common`, `docker`, `database`, `webapp`, `voip`, `firewall` et `verification`.

L’objectif est de pouvoir relancer le playbook plusieurs fois sans modifier inutilement une configuration déjà correcte.

## Sécurité

Un pare-feu sera utilisé afin de limiter les accès aux services nécessaires.

Les principaux ports prévus sont SSH pour l’administration, HTTP pour l’application web, SIP pour la signalisation téléphonique et RTP pour l’audio.

MariaDB ne sera pas directement accessible depuis le réseau utilisateur. L’application Flask communiquera avec la base depuis le réseau Docker interne.

## Tests prévus

Plusieurs tests permettront de vérifier le fonctionnement du projet.

Pour l’application, les tests porteront notamment sur la recherche d’un client, l’affichage de ses informations et la création d’un ticket.

Pour la partie VoIP, les premiers tests porteront sur les appels entre les extensions 101 et 102, les appels via le trunk SIP, le comportement d’un trunk indisponible et le cas d’un poste SIP non enregistré.
