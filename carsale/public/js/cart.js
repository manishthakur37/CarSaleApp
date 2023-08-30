// cart.js

const cart = [];

function addToCart(carId) {
    const car = document.querySelector(`[data-car-id="${carId}"]`);
    const carInfo = {
        id: carId,
        make: car.getAttribute('data-brand'),
        model: car.getAttribute('data-model'),
        year: car.getAttribute('data-year'),
        price: car.getAttribute('data-price'),
    };
    cart.push(carInfo);
    updateCartCount();
}

function updateCartCount() {
    const cartCount = document.getElementById('cartCount');
    cartCount.textContent = cart.length;
}

// Event listener for "Add to Cart" buttons
document.addEventListener('click', event => {
    if (event.target.classList.contains('add-to-cart-button')) {
        const carId = event.target.closest('.product-card').getAttribute('data-car-id');
        addToCart(carId);
    }
});

// Initialization
updateCartCount();