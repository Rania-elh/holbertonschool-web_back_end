import redis from 'redis';

// Client Redis (localhost:6379 par défaut)
const client = redis.createClient();

function onConnect() {
  console.log('Redis client connected to the server');
}

function onError(err) {
  console.log(`Redis client not connected to the server: ${err}`);
}

client.on('connect', onConnect);
client.on('error', onError);
