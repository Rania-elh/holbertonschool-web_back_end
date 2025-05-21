const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf-8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  // Découper en lignes et enlever lignes vides (trim en début et fin)
  const lines = data.trim().split('\n');
  // Supprimer la première ligne d'en-tête
  const students = lines.slice(1).filter(line => line.trim() !== '');

  console.log(`Number of students: ${students.length}`);

  const fields = {};

  for (const line of students) {
    const parts = line.split(',');
    if (parts.length < 4) continue; // ligne malformée ignorée

    const firstName = parts[0].trim();
    const field = parts[3].trim();

    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstName);
  }

  for (const field in fields) {
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
  }
}

module.exports = countStudents;
