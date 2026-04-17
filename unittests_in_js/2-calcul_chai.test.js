const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  describe('SUM', () => {
    const aValues = [0, 0.1, 0.4, 0.5, 0.51, 1.2, 1.5, 2.3, 2.5];
    const bValues = [0, 0.2, 0.49, 0.5, 0.7, 1.49, 1.5, 2.4, 2.5];

    aValues.forEach((a) => {
      bValues.forEach((b) => {
        it(`returns ${Math.round(a) + Math.round(b)} for a=${a}, b=${b}`, () => {
          expect(calculateNumber('SUM', a, b)).to.equal(Math.round(a) + Math.round(b));
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
          expect(calculateNumber('SUBTRACT', a, b)).to.equal(Math.round(a) - Math.round(b));
        });
      });
    });
  });

  describe('DIVIDE', () => {
    it('returns Error when b rounds to 0 (b=0)', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('returns Error when b rounds to 0 (b=0.2)', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
    });

    it('divides rounded a by rounded b', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(1 / 5);
    });

    const aValues = [0, 0.1, 0.4, 0.5, 0.51, 1.2, 1.5, 2.3, 2.5];
    const bValues = [0.5, 0.7, 1.1, 1.49, 1.5, 1.51, 2.4, 2.5];

    aValues.forEach((a) => {
      bValues.forEach((b) => {
        const expected = Math.round(a) / Math.round(b);
        it(`returns ${expected} for a=${a}, b=${b}`, () => {
          expect(calculateNumber('DIVIDE', a, b)).to.equal(expected);
        });
      });
    });
  });
});

