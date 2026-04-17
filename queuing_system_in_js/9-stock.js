import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  let numId = id;
  if (typeof id !== 'number') {
    numId = parseInt(id, 10);
  }
  for (let i = 0; i < listProducts.length; i += 1) {
    if (listProducts[i].id === numId) {
      return listProducts[i];
    }
  }
  return undefined;
}

const redisClient = redis.createClient();

const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

function onRedisError(err) {
  console.log(`Redis client not connected to the server: ${err}`);
}

redisClient.on('error', onRedisError);

function redisItemKey(itemId) {
  return `item.${itemId}`;
}

async function reserveStockById(itemId, stock) {
  const key = redisItemKey(itemId);
  await setAsync(key, String(stock));
}

async function getCurrentReservedStockById(itemId) {
  const key = redisItemKey(itemId);
  const raw = await getAsync(key);
  if (raw === null || raw === undefined) {
    return 0;
  }
  const n = parseInt(raw, 10);
  if (Number.isNaN(n)) {
    return 0;
  }
  return n;
}

const app = express();

app.get('/list_products', function listProductsRoute(req, res) {
  const out = [];
  for (let i = 0; i < listProducts.length; i += 1) {
    const p = listProducts[i];
    out.push({
      itemId: p.id,
      itemName: p.name,
      price: p.price,
      initialAvailableQuantity: p.stock,
    });
  }
  res.json(out);
});

app.get('/list_products/:itemId', async function productDetailRoute(req, res) {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }
  const reserved = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - reserved;
  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async function reserveRoute(req, res) {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }
  const reserved = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - reserved;
  if (currentQuantity < 1) {
    res.json({ status: 'Not enough stock available', itemId: itemId });
    return;
  }
  const newReserved = reserved + 1;
  await reserveStockById(itemId, newReserved);
  res.json({ status: 'Reservation confirmed', itemId: itemId });
});

app.listen(1245, function onListen() {
  console.log('Server listening on port 1245');
});
