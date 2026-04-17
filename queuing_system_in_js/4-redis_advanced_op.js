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

const hashKey = 'HolbertonSchools';

// paires [champ, valeur] pour remplir le hash
const rows = [
  ['Portland', '50'],
  ['Seattle', '80'],
  ['New York', '20'],
  ['Bogota', '20'],
  ['Cali', '40'],
  ['Paris', '2'],
];

for (let i = 0; i < rows.length; i += 1) {
  const field = rows[i][0];
  const value = rows[i][1];
  client.hset(hashKey, field, value, redis.print);
}

function afterHgetall(err, value) {
  console.log(value);
}

client.hgetall(hashKey, afterHgetall);
