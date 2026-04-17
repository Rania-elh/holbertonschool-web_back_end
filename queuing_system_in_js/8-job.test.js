import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function describeJobs() {
  let queue;

  before(function setupQueue() {
    queue = kue.createQueue();
    queue.on('error', function ignoreRedisError() {});
    queue.testMode.enter();
  });

  afterEach(function clearJobs() {
    queue.testMode.clear();
  });

  after(function teardownQueue() {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', function testNotArray() {
    expect(function callWithObject() {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');

    expect(function callWithString() {
      createPushNotificationsJobs('not an array', queue);
    }).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', function testTwoJobs() {
    const twoJobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518782',
        message: 'This is the code 4321 to verify your account',
      },
    ];

    createPushNotificationsJobs(twoJobs, queue);

    expect(queue.testMode.jobs).to.have.lengthOf(2);

    for (let i = 0; i < queue.testMode.jobs.length; i += 1) {
      const job = queue.testMode.jobs[i];
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.eql(twoJobs[i]);
    }
  });
});
