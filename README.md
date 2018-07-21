# Docker-Jailer-Python
Docker jail system based on the FreeBSD and BSD Jail system.

Utilize with a HoneyPot preferably Artillery. Redirect any would be attackers into the docker container(fully virtualized enviroment which mimics the host system as best as it can) Attackers are then isolated away from the host system in a nullFS style system in which they cannot do any actual harm to the host system itself, after the attacker has exited pilfering what they think is encrypted data, you can trash the docker container and start a new one, rinse and repeat.
