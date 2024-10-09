const form = document.getElementById('data-form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;

    try {
        const response = await fetch('http://127.0.0.1:5000/submit', {  // Changed the URL to point to backend
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        console.log(result);
        alert(result.message); // Example of displaying success message
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        alert('There was an error submitting the form. Please try again.'); // Example of displaying error message
    }
});
