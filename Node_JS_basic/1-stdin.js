process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  console.log(`Your name is: ${name}`);
  console.log('This important notification is brought to you by the Holberton School');
  process.stdin.end();
});
