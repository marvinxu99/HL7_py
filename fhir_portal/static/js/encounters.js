document.addEventListener('DOMContentLoaded', function () {
    // Fetch the encounters from the Flask API
    fetch('/api/encounters')
        .then(response => response.json())
        .then(data => {
            const encounterList = document.getElementById('encounter-list');
            data.forEach(encounter => {
                const li = document.createElement('li');
                li.textContent = `Encounter ID: ${encounter.id}, Status: ${encounter.status}`
                li.textContent += `St: ${encounter.id}, Status: ${encounter.status}`
                encounterList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching encounters:', error));
});
// li.textContent = `Encounter ID: ${encounter.id}, Status: ${encounter.status}, Type: ${encounter.type[0]?.text || 'Unknown'}`;
