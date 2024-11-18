async function generateBio() {
    const career = document.getElementById("career").value;
    const personality = document.getElementById("personality").value;
    const interests = document.getElementById("interests").value;
    const goals = document.getElementById("goals").value;

    try {
        const response = await fetch('/generate_bio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',  // Ensure correct Content-Type
            },
            body: JSON.stringify({ 
                career, 
                personality, 
                interests, 
                goals 
            }),
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error(`Server Error: ${response.status} - ${errorText}`);
            alert("Failed to generate bio. Please check the console for details.");
            return;
        }

        const result = await response.json();
        if (result.bio) {
            document.getElementById("bioOutput").textContent = result.bio;
        } else {
            console.error("Unexpected response format:", result);
            alert("Bio generation failed. Please try again.");
        }
    } catch (error) {
        console.error("Fetch request failed:", error);
        alert("An error occurred while generating the bio. Please check the console for details.");
    }
}
