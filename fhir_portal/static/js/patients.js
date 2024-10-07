document.addEventListener('DOMContentLoaded', function () {
    // Fetch the patients from the Flask API
    fetch('/api/patients')
        .then(response => response.json())
        .then(data => {
            const patientList = document.getElementById('patient-list');
            data.forEach(patient => {
                const li = document.createElement('li');
                li.textContent = `Name: ${patient.name[0].given[0]} ${patient.name[0].family} - Gender: ${patient.gender ? patient.gender : 'n/a'}`;
                patientList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching patients:', error));
});
