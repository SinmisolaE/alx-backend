import { createClient, print } from 'redis';
import { promisify } from 'utils';

const client = createClient();
client.on('connect', function() {
  console.log('Redis client connected to the server');
}).on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const result = await (get(schoolName).catch((error) => {
    if(error) {
      console.log(error);
      return;
    }
  });
  console.log(result);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
