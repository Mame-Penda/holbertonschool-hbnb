document.addEventListener('DOMContentLoaded', () => {
    const token = getCookie('token');
    const placeId = getPlaceIdFromURL();
  
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
      reviewForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const reviewText = document.getElementById('review').value.trim();
  
        if (!reviewText) {
          alert('Please enter a review');
          return;
        }
  
        await submitReview(token, placeId, reviewText);
      });
    }
  });
  
  /* Simule récupération de cookie */
  function getCookie(name) {
    const cookieArr = document.cookie.split(';');
    for (const cookie of cookieArr) {
      const [key, value] = cookie.trim().split('=');
      if (key === name) return value;
    }
    return null;
  }
  
  /* Simule l'extraction de place_id depuis l'URL */
  function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
  }
  
  /* POST la review */
  async function submitReview(token, placeId, reviewText) {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/v1/reviews/', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          text: reviewText,
          place_id: placeId
        })
      });
  
      handleResponse(response);
    } catch (error) {
      console.error('Network error:', error);
      alert('Network error');
    }
  }
  
  /* Réponse du serveur */
  function handleResponse(response) {
    if (response.ok) {
      alert('Review submitted successfully!');
      document.getElementById('review-form').reset();
    } else {
      alert('Failed to submit review');
    }
  }
  