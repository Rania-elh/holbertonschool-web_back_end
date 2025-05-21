// Prompt the user with a welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Flag to check if name has been output to avoid multiple outputs
let nameDisplayed = false;

// Listen for data input from stdin (user input)
process.stdin.on('data', (data) => {
  if (!nameDisplayed) {
    const name = data.toString().trim();
    process.stdout.write(`Your name is: ${name}\n`);
    nameDisplayed = true;
  }
});

// Listen for the end of the input stream (e.g. pipe finished or Ctrl+D)
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});

// If input is from terminal, listen for Ctrl+D (end of input)
if (process.stdin.isTTY) {
  process.stdin.resume();
}
