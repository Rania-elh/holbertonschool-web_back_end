const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  const aValues = [
    0,
    0.1,
    0.2,
    0.4,
    0.49,
    0.5,
    0.51,
    1.2,
    1.5,
    1.7,
    2.3,
    2.5,
    2.8,
  ];

  const bValues = [
    0,
    0.2,
    0.5,
    0.7,
    1.1,
    1.49,
    1.5,
    1.51,
    2.4,
    2.5,
  ];

  aValues.forEach((a) => {
    bValues.forEach((b) => {
      it(`returns ${Math.round(a) + Math.round(b)} for a=${a}, b=${b}`, () => {
        assert.strictEqual(calculateNumber(a, b), Math.round(a) + Math.round(b));
      });
    });
  });
});

