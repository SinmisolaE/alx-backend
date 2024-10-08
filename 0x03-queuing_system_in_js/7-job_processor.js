import {createQueue} from 'kue';

const blacklist = ['4153518780', '4153518781'];

const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(`Sending notification to PHONE_NUMBER, with message: ${message}`);
}

queue.process(push_notification_code_2, 2, function(job, done) {
  sendNotification(job.data.phoneNumber, job.data.message, done);
});
