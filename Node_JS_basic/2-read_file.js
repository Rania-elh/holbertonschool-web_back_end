const fs = require('fs');

function countStudents(path) {
  let data;

  try {
    data = fs.readFileSync(path, 'utf-8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  // Split by lines, trim to remove trailing newlines, and filter empty lines
  const lines = data.trim().split('\n');

  // Remove header
  const students = lines.slice(1).filter(line => line.trim() !== '');

  console.log(`Number of students: ${students.length}`);

  const fields = {};

  for (const student of students) {
    const parts = student.split(',');

    if (parts.length < 4) continue; // Ignore malformed lines

    const firstName = parts[0].trim();
    const field = parts[3].trim();

    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstName);
  }

  // Print students per field sorted in order of appearance
  for (const field of Object.keys(fields)) {
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
  }
}

module.exports = countStudents;
