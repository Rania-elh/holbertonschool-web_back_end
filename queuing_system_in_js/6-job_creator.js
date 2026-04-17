import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData);

function onComplete() {
  console.log('Notification job completed');
}

function onFailed() {
  console.log('Notification job failed');
}

job.on('complete', onComplete);
job.on('failed', onFailed);

function afterSave(err) {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
}

job.save(afterSave);
