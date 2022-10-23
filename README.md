# Hackers Teaching Hackers 2022 CTF

This repository contains challenge source code used in the Hackers Teaching Hackers (HTH) Capture the Flag (CTF) for 2022.

# Installing dependencies

Run the following commands to get everything configured on your system. Tested on Ubuntu 22.04.1 LTS.

```
sudo apt install git
git clone https://gitlab.com/hackers-teaching-hackers/hthctf2022
cd HTHCTF2022/src/scripts/
chmod +x install_deps.sh
./install_deps.sh
```

# Start challenge set with docker-compose

Run this to blow all Docker images and containers away.
```
docker-compose up       # Run and monitor
docker-compose up -d    # Run as daemon
```

# Nuking docker 

Run this to blow all Docker images and containers away.
```
docker system prune -a
```