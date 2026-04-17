const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  describe('SUM', () => {
    const aValues = [0, 0.1, 0.4, 0.5, 0.51, 1.2, 1.5, 2.3, 2.5];
    const bValues = [0, 0.2, 0.49, 0.5, 0.7, 1.49, 1.5, 2.4, 2.5];

    aValues.forEach((a) => {
      bValues.forEach((b) => {
        it(`returns ${Math.round(a) + Math.round(b)} for a=${a}, b=${b}`, () => {
          assert.strictEqual(
            calculateNumber('SUM', a, b),
            Math.round(a) + Math.round(b),
          );
        });
      });
    });
  });

  describe('SUBTRACT', () => {
    const aValues = [0, 0.1, 0.4, 0.5, 0.51, 1.2, 1.5, 2.3, 2.5];
    const bValues = [0, 0.2, 0.49, 0.5, 0.7, 1.49, 1.5, 2.4, 2.5];

    aValues.forEach((a) => {
      bValues.forEach((b) => {
        it(`returns ${Math.round(a) - Math.round(b)} for a=${a}, b=${b}`, () => {
          assert.strictEqual(
            calculateNumber('SUBTRACT', a, b),
            Math.round(a) - Math.round(b),
          );
        });
      });
    });
  });

  describe('DIVIDE', () => {
    it('returns Error when b rounds to 0 (b=0)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('returns Error when b rounds to 0 (b=0.2)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error');
    });

    it('divides rounded a by rounded b', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 1 / 5);
    });

    const aValues = [0, 0.1, 0.4, 0.5, 0.51, 1.2, 1.5, 2.3, 2.5];
    const bValues = [0.5, 0.7, 1.1, 1.49, 1.5, 1.51, 2.4, 2.5];

    aValues.forEach((a) => {
      bValues.forEach((b) => {
        const expected = Math.round(a) / Math.round(b);
        it(`returns ${expected} for a=${a}, b=${b}`, () => {
          assert.strictEqual(calculateNumber('DIVIDE', a, b), expected);
        });
      });
    });
  });
});

