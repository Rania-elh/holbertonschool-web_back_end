function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (let i = 0; i < jobs.length; i += 1) {
    const data = jobs[i];
    const job = queue.create('push_notification_code_3', data);

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
}

export default createPushNotificationsJobs;
