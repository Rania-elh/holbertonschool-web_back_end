// Prompt the user with a welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Listen for data input from stdin (user input)
process.stdin.on('data', (data) => {
  // Convert the input buffer to a string and remove any trailing newline characters
  const name = data.toString().trim();
  // Output the user's name
  process.stdout.write(`Your name is: ${name}\n`);
});

// Listen for the end of the input stream (when user ends the program or pipe finishes)
process.stdin.on('end', () => {
  // Notify that the software is closing
  process.stdout.write('This important software is now closing\n');
});
