document.getElementById('delete-profile-btn').addEventListener('click', function () {
    if (confirm('Are you sure you want to delete your profile?')) {
        // If the user confirms, make an AJAX request to delete the profile
        fetch('{% url "profile-delete" %}', {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}', // Add CSRF token for security
            },
        })
            .then(response => {
                if (response.ok) {
                    // Profile deleted successfully, redirect to home page
                    alert('Profile deleted successfully.');
                    window.location.href = '{% url "home-page" %}';
                } else if (response.status === 403) {
                    // User is not authorized to delete profile (error message from server)
                    return response.json().then(data => {
                        alert(data.message);
                    });
                } else {
                    // Handle other errors, show a message, etc.
                    alert('Error deleting profile.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});
