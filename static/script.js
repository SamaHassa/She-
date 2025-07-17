document.querySelectorAll('.remove-btn').forEach(button => {
  button.addEventListener('click', function () {
    this.closest('.cart-item').remove();

    // Optional: check if cart is now empty
    const cartItems = document.querySelectorAll('.cart-item');
    if (cartItems.length === 0) {
      document.getElementById('emptyCart').style.display = 'block';
      document.getElementById('checkoutBox').style.display = 'none';
    }
  });
});




function showSection(id) {
  document.querySelectorAll('.dashboard-section').forEach(section => {
      section.classList.remove('active');});
      document.getElementById(id).classList.add('active');
    }
