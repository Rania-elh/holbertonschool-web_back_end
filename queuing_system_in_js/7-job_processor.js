import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    const msg = `Phone number ${phoneNumber} is blacklisted`;
    done(new Error(msg));
    return;
  }

  job.progress(50, 100);

  const line = `Sending notification to ${phoneNumber}, with message: ${message}`;
  console.log(line);

  done();
}

const queue = kue.createQueue();

function processOneJob(job, done) {
  sendNotification(
    job.data.phoneNumber,
    job.data.message,
    job,
    done,
  );
}

// le 2 = deux jobs en même temps
queue.process('push_notification_code_2', 2, processOneJob);
