const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf-8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.trim().split('\n');

  // Enlever la ligne d'en-tête
  const students = lines.slice(1).filter(line => line.trim() !== '');

  console.log(`Number of students: ${students.length}`);

  const fields = {};

  students.forEach(line => {
    const parts = line.split(',');
    if (parts.length < 4) return; // ignore malformed lines

    const firstName = parts[0].trim();
    const field = parts[3].trim();

    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstName);
  });

  for (const field in fields) {
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
  }
}

module.exports = countStudents;
