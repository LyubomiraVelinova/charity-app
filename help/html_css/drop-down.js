// Function to toggle the dropdown menu
function toggleDropdown(event) {
      // Get the corresponding dropdown content
    const dropdownContent = event.target.nextElementSibling;
    // Toggle the "show" class to display or hide the dropdown content
    dropdownContent.classList.toggle('show');
}


// Get all dropdown toggle buttons
const dropdownToggleBtns = document.querySelectorAll(".dropbtn");

// Add click event listener to each dropdown toggle button
dropdownToggleBtns.forEach(function (btn) {
    btn.addEventListener('click', toggleDropdown);
});

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
};