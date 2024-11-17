document.getElementById('bioForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const career = document.getElementById('career').value;
    const personality = document.getElementById('personality').value;
    const interests = document.getElementById('interests').value;
    const goals = document.getElementById('goals').value;

    try {
        const response = await fetch('/generate_bio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ career, personality, interests, goals }),
        });

        const result = await response.json();

        if (result.bio) {
            document.getElementById('bioText').textContent = result.bio;
        } else {
            document.getElementById('bioText').textContent = 'Error generating bio. Please try again.';
        }
    } catch (error) {
        document.getElementById('bioText').textContent = 'Error connecting to the server.';
    }
});
