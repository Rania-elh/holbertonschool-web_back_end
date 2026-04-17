const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  const url = 'http://localhost:7865/';

  it('should return status code 200', (done) => {
    request.get(url, (err, res) => {
      expect(err).to.equal(null);
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the right result', (done) => {
    request.get(url, (err, _res, body) => {
      expect(err).to.equal(null);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should return a string body', (done) => {
    request.get(url, (err, _res, body) => {
      expect(err).to.equal(null);
      expect(body).to.be.a('string');
      done();
    });
  });
});

describe('Cart page', () => {
  it('should return status code 200 when :id is a number', (done) => {
    request.get('http://localhost:7865/cart/12', (err, res) => {
      expect(err).to.equal(null);
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the right result when :id is a number', (done) => {
    request.get('http://localhost:7865/cart/12', (err, _res, body) => {
      expect(err).to.equal(null);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 when :id is NOT a number', (done) => {
    request.get('http://localhost:7865/cart/hello', (err, res) => {
      expect(err).to.equal(null);
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});

