# Réunion WhatsApp le 27/06 avec Omer Nguena Timo

### Objectifs pour le 29/06

#### LSTM pour prédire un groupe de mots
Regarder le vecteurs de sortie du réseau pour prédire un groupe de mots et non un mot unique. On cherche à pouvoir choisir parmis un ensemble de mots plutôt qu'avoir un unique mot imposé.

#### Installer Security Onion
- Installer Security Onion
- Comprendre son architecture et les fonctions des outils qui le compose
- Configurer un réseau
- Récolter du trafic réseau

#### Rapport de recherche
Commencer à rédiger un rapport sur les LSTM, embedding, et le code réalisé. (environ 2 pages)

### Réalisation

##### Installer Security Onion
- Première tentative avec une VM Security Onion  

Comme la VM demande 12GO de RAM, il n'en reste que 4 pour le PC et cela n'est pas convenable. Il est impossible de travailler ou d'utiliser le PC, et même la VM fini par bugger.

- Installation de Security Onion directement sur Ubuntu  

Installation de Security Onion, mais problème lors de l'initialisation.
Il est nécessaire d'avoir 2 interfaces réseaux pour utiliser Security Onion. J'ai donc configuré une interface réseau virtuelle (Cf https://linuxconfig.org/configuring-virtual-network-interfaces-in-linux). Cependant, cela ne correspond pas à ce qui est nécessaire, il faut donc la configurer pour qu'elle corresponde à un réseau interne.

L'erreur trouvée lors de l'analyse des log de l'installation est la suivante : 
```bash
2022-06-27T22:26:10Z | I | Executing command: ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp3s0f1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 70:8b:cd:12:9f:dd brd ff:ff:ff:ff:ff:ff
3: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 48:45:20:d6:79:05 brd ff:ff:ff:ff:ff:ff
    inet 192.168.2.82/24 brd 192.168.2.255 scope global dynamic noprefixroute wlp2s0
       valid_lft 258331sec preferred_lft 258331sec
    inet6 fe80::da96:4156:7ca3:85d5/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
4: eth0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default qlen 1000
    link/ether c8:d7:4a:4e:47:50 brd ff:ff:ff:ff:ff:ff
    inet 192.168.2.98/24 brd 192.168.2.255 scope global eth0:0
       valid_lft forever preferred_lft forever
Beginning Security Onion network install
Setup is running on TTY /dev/pts/0
2022-06-27T22:26:24Z | I | Disabling ipv6
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
ERROR: Could not determine MAINIP or MNIC_IP.
MAINIP=192.168.2.82
MNIC_IP=
```

MNIC_IP 

#### Vecteurs d'embedding