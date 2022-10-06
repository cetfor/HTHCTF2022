# Hackers Teaching Hackers 2022 CTF

This repository contains challenge source code used in the Hackers Teaching Hackers (HTH) Capture the Flag (CTF) for 2022.

# Installing Dependencies

Run the following commands to get everything configured on your system. Tested on Ubuntu 22.04.1 LTS.

```
sudo apt install git
git pull https://github.com/cetfor/HTHCTF2022
cd HTHCTF2022/src/scripts/
chmod +x install_deps.sh
./install_deps.sh
```

# Configuring RCTF

This CTF uses the [RCTF](https://rctf.redpwn.net/) platform by [Redpwn](https://redpwn.net/). Running the installation script (`install_deps.sh`) will install RCTF to `/opt/rctf` and start the RCTF Docker conatiner. You can access the RCTF platform by browsing to `http://127.0.0.1:8080`. 

This will launch RCTF with a default configuration. We can customize the installation by modifying the `yaml` files in `/opt/rctf/conf.d/`. These files are:

```
/opt/rctf/conf.d/01-ui.yaml     # Basic CTF description, image, home page content
/opt/rctf/conf.d/02-ctf.yaml    # CTF start time, end time, token key, divisions, origin URL
/opt/rctf/conf.d/03-db.yaml     # Database configuration options
```

You can find detailed configuration options and instructions at [https://rctf.redpwn.net/configuration/](https://rctf.redpwn.net/configuration/).

