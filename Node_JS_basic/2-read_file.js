const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    // Read file synchronously
    data = fs.readFileSync(path, 'utf-8');
  } catch (err) {
    // If reading fails, throw error
    throw new Error('Cannot load the database');
  }

  // Split the file content by new line
  const lines = data.trim().split('\n');

  // Remove header line (first line)
  const students = lines.slice(1).filter(line => line.trim() !== '');

  // Count total students
  console.log(`Number of students: ${students.length}`);

  // Object to store students by field
  const fields = {};

  // Process each student line
  students.forEach((line) => {
    const parts = line.split(',');

    // Format CSV assumed: firstname,lastname,age,field
    const firstName = parts[0].trim();
    const field = parts[3].trim();

    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstName);
  });

  // Display number of students and list per field
  for (const field in fields) {
    const list = fields[field].join(', ');
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
  }
}

module.exports = countStudents;
