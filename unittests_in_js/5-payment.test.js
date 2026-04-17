const sinon = require('sinon');
const { expect } = require('chai');

const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let logSpy;

  beforeEach(() => {
    logSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    logSpy.restore();
  });

  it('logs "The total is: 120" when called with 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);

    expect(logSpy.calledOnce).to.equal(true);
    expect(logSpy.calledWithExactly('The total is: 120')).to.equal(true);
  });

  it('logs "The total is: 20" when called with 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);

    expect(logSpy.calledOnce).to.equal(true);
    expect(logSpy.calledWithExactly('The total is: 20')).to.equal(true);
  });
});

