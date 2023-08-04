function toggleAdditionalText(linkElement, event) {
    event.preventDefault(); // Prevent the default behavior of the link
    let cardBody = linkElement.parentNode; // Get the parent node of the link (card-body)
    let shortText = cardBody.querySelector('.short-text');
    let additionalText = cardBody.querySelector('.additional-text');
    let moreLabel = cardBody.querySelector('.more-label');

    additionalText.classList.toggle('hidden');
    shortText.classList.toggle('hidden');
    moreLabel.textContent = additionalText.classList.contains('hidden') ? '...Learn More' : 'Less';
}

//HERE
