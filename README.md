# Hackers Teaching Hackers 2022 CTF

This repository contains challenge source code used in the Hackers Teaching Hackers (HTH) Capture the Flag (CTF) for 2022.

# Installing dependencies

Run the following commands to get everything configured on your system. Tested on Ubuntu 22.04.1 LTS.

```
sudo apt install git
git clone https://github.com/cetfor/HTHCTF2022
cd HTHCTF2022
chmod +x HTHCTF2022/src/scripts/install_deps.sh
./HTHCTF2022/src/scripts/install_deps.sh
```

# Building the Docker containers

Run this to build all Docker images.
```
docker-compose build             # build using layer cache
docker-compose build --no-cache  # build without cache
```

# Start challenge set with docker-compose

Run this to start all Docker containers.
```
docker-compose up       # Run and monitor
docker-compose up -d    # Run as daemon
```

# Nuking docker 

Run this to blow all Docker images and containers away.
```
docker system prune -a
```
