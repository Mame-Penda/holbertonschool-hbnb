function getPlaceIdFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('id');
}
function checkAuthentification() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById("add-review") || document.querySelector('.submit-review');

    if (!token) {
        if (addReviewSection) addReviewSection.style.display = "none";
        return null;
    } else {
        if (addReviewSection) addReviewSection.style.display = "block";
        return token;
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`https://api.example.com/places/${placeId}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
            }
    });
    
    if (response.ok) {
        const place = await response.json();
        displayPlaceDetails(place);
    } else {
        console.error('Error fetching place details:', response.status);
    }
} catch (error) {
    console.error('Network error:', error);
}
}

function displayPlaceDetails(place) {
    const placeDetailsSection = document.getElementById("place-details");
    placeDetailsSection.innerHTML= '';

    const placeName = document.createElement("h1");
    placeName.innerText = place.name;

    const placePrice = document.createElement('p');
    placePrice.innerText = `Price per night: €${place.price}`;
    
    const placeDescription = document.createElement('p');
    placeDescription.innerText = `Description: ${place.description}`;

    const amenitiesTitle = document.createElement('h2');
    amenitiesTitle.innerText = "Amenities";

    const amenitiesList = document.createElement('ul');
    amenitiesList.id = 'place-amenities';

    place.amenities.forEach(amenity => {
        const item = document.createElement('li');
        item.innerText = amenity;
        amenitiesList.appendChild(item);
});

placeDetailsSection.appendChild(placeName, placePrice, placeDescription, amenitiesTitle, amenitiesList);

}

const logoutBtn = document.getElementById("logout");
if (logoutBtn) {
    logoutBtn.onclick = () => {
        document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        window.location.href = "login.html";
    };
}

document.addEventListener("DOMContentLoaded", () => {
    const token = checkAuthentification();
    const placeId = getPlaceIdFromURL();

    if (token && placeId) {
        fetchPlaceDetails(token, placeId);
    } else {
        window.location.href = "login.html";
    }
});