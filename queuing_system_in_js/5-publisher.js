import redis from 'redis';

const channelName = 'holberton school channel';

const client = redis.createClient();

function onConnect() {
  console.log('Redis client connected to the server');
}

function onError(err) {
  console.log(`Redis client not connected to the server: ${err}`);
}

client.on('connect', onConnect);
client.on('error', onError);

function publishMessage(message, timeMs) {
  function sendLater() {
    console.log(`About to send ${message}`);
    client.publish(channelName, message);
  }
  setTimeout(sendLater, timeMs);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
