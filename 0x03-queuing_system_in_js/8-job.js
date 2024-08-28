function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }
  jobs.forEach((ajob) => {
    let job = queue.create(push_notification_code_3, ajob);
    job.on('complete', function() {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', function(error) {
      console.log(`Notification job ${job.is} failed: ${error}`);
    }).on('progress', function(progress, data) {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
    job.save((error) => {
      if (!error) console.log(`Notification job created: ${job.id}`);
    });
  });
}

module.exports = createPushNotificationsJobs;
