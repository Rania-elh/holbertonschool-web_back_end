const fs = require('fs');

/**
 * Counts the students in a CSV file and logs stats.
 * @param {string} path - Path to the CSV database file.
 */
function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const header = lines.shift().split(',');

    const fieldIndex = header.length - 1;
    const studentsByField = {};
    let total = 0;

    for (const line of lines) {
      const parts = line.split(',');
      if (parts.length === header.length) {
        total += 1;
        const field = parts[fieldIndex];
        const firstName = parts[0];

        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstName);
      }
    }

    console.log(`Number of students: ${total}`);
    for (const [field, names] of Object.entries(studentsByField)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
