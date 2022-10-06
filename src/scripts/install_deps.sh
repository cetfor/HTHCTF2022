# Update the system
sudo apt update

# Install Docker (https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)
sudo apt -y install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt -y install docker-ce
sudo apt -y install docker-compose
sudo apt -y install python3-pip

# Install required pip packages
pip3 install rcds

# Ability to run Docker without sudo
sudo usermod -aG docker ${USER}

# Make sure Docker is installed correctly
docker run hello-world

# Install RCTF (installs to /opt/rctf, `run docker ps -l` to see running Docker container)
curl https://get.rctf.redpwn.net | sudo sh
