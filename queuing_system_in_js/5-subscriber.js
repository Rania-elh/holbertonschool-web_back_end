import redis from 'redis';

const channelName = 'holberton school channel';

const client = redis.createClient();

function onConnect() {
  console.log('Redis client connected to the server');
}

function onError(err) {
  console.log(`Redis client not connected to the server: ${err}`);
}

function onMessage(channel, message) {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channelName);
    client.quit();
  }
}

client.on('connect', onConnect);
client.on('error', onError);
client.on('message', onMessage);

client.subscribe(channelName);
