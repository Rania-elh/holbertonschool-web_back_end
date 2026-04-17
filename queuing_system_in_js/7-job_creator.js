import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const queue = kue.createQueue();

for (let i = 0; i < jobs.length; i += 1) {
  const oneJobData = jobs[i];
  const job = queue.create('push_notification_code_2', oneJobData);

  function onComplete() {
    console.log(`Notification job ${job.id} completed`);
  }

  function onFailed(errorMessage) {
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  }

  function onProgress(progress) {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  }

  job.on('complete', onComplete);
  job.on('failed', onFailed);
  job.on('progress', onProgress);

  function afterSave(err) {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  }

  job.save(afterSave);
}
