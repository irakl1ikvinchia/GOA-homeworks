let cart = [];

    function addToCart(productName, productPrice) {
        cart.push({ name: productName, price: productPrice });
        updateCart();
    }

    function updateCart() {
        const cartDiv = document.getElementById('cart');
        cartDiv.innerHTML = ''; // ცარიელდება კალათის სექცია

        if (cart.length === 0) {
            cartDiv.innerHTML = '<p>კალათი ცარიელია.</p>';
        } else {
            cart.forEach(item => {
                cartDiv.innerHTML += `<p>${item.name} - ${item.price} ლარი</p>`;
            });
        }
    }