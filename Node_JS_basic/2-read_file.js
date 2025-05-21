const fs = require('fs');

/**
 * Count students from a CSV file and display statistics.
 * @param {string} path - The path to the CSV database file.
 * @throws Will throw an error if the database cannot be loaded.
 */
function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const students = lines.slice(1); // Remove header line
    console.log(`Number of students: ${students.length}`);

    const fields = {};

    for (const student of students) {
      const parts = student.split(',');
      const firstname = parts[0].trim();
      const field = parts[3].trim();

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }

    for (const field in fields) {
      const list = fields[field].join(', ');
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
