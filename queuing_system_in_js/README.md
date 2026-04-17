# File d’attente en JS

## Redis

Le fichier **`dump.rdb`** est dans ce dossier. Lance Redis **depuis ce dossier** (pour charger le fichier), puis teste :

```bash
redis-cli get Holberton
```

Tu dois voir : `"School"`.

### Installer Redis 6.0.10

```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
src/redis-server &
src/redis-cli ping
```

`ping` doit répondre **PONG**. Pour arrêter : `ps aux | grep redis-server` puis `kill` avec le bon PID.

Le `dump.rdb` ici vient de Redis 6.0.10 avec la clé **Holberton** = **School**.
