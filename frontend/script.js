document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('bfhl-form');
    const dataInput = document.getElementById('data-input');
    const responseContainer = document.getElementById('response-container');
    const responseDisplay = document.getElementById('response-display');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const inputData = dataInput.value.split(',').map(item => item.trim());
        const apiUrl = 'http://127.0.0.1:5000/bfhl'; // Adjust if your Flask app runs on a different port/host

        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ data: inputData }),
            });

            const result = await response.json();

            if (response.ok) {
                responseDisplay.textContent = JSON.stringify(result, null, 2);
                responseContainer.classList.remove('hidden');
            } else {
                responseDisplay.textContent = `Error: ${result.error || response.statusText}`;
                responseContainer.classList.remove('hidden');
            }
        } catch (error) {
            responseDisplay.textContent = `Network Error: ${error.message}`;
            responseContainer.classList.remove('hidden');
        }
    });
});
