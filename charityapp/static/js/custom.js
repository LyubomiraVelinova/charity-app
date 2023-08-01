// SEARCH
// NOT WORKING
function toggleSearchInput() {
    let searchInput = document.getElementById('searchInput');
    searchInput.classList.toggle('show');
}

function toggleAdditionalText() {
    let additionalText = document.getElementById('additionalText');
    let moreLabel = document.getElementById('moreLabel');

    additionalText.classList.toggle('hidden');
    moreLabel.textContent = additionalText.classList.contains('hidden') ? 'More' : 'Less';
}


