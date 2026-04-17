import redis from 'redis';

const client = redis.createClient();

function onConnect() {
  console.log('Redis client connected to the server');
}

function onError(err) {
  console.log(`Redis client not connected to the server: ${err}`);
}

client.on('connect', onConnect);
client.on('error', onError);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  function afterGet(err, reply) {
    console.log(reply);
  }
  client.get(schoolName, afterGet);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
