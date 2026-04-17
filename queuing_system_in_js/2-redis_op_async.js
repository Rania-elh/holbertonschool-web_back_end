import { promisify } from 'util';
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

// get() devient une fonction async grâce à promisify
const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const reply = await getAsync(schoolName);
  console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
