import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  const line = `Sending notification to ${phoneNumber}, with message: ${message}`;
  console.log(line);
}

function processOneJob(job, done) {
  const phone = job.data.phoneNumber;
  const text = job.data.message;
  sendNotification(phone, text);
  done();
}

queue.process('push_notification_code', processOneJob);
