# DoomsDay
Docker jail system based on the FreeBSD and BSD Jail system, the ultimate doomsday device for information security.

Utilize with a HoneyPot preferably [Artillery](https://github.com/BinaryDefense/artillery).  
Redirect any would be attackers into the docker container (fully virtualized environment that mimics the host system as best as it can - of course you as the user have to configure it that way, inside the dockerfile.yml file and the actual DockerFile).  
Attackers are then isolated away from the host system in a nullFS style system in which they cannot do any actual harm to the host system itself, after the attacker has exited pilfering what they think is encrypted data, you can trash the docker container and start a new one, rinse and repeat.

# Honey Do List:
- Create Function to spin up docker container upon calling of the script.
- Cloak the presence of the docker container.
- Simulate admin activity within the container.
- Simulate traffic to and from the container.

# Disclaimer

As this script is still under development, it is greatly appriciated if you as a potential user of this wonderful program would report the issues you find here, so they can be fixed and make this program an amazing suppliment to your organizations security!  
Thank you very much in advance.
