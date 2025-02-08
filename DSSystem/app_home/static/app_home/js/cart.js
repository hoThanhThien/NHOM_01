// Lấy tất cả nút "Add to Cart"
var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('Product ID:', productId, '| Action:', action);
        console.log('User:', user);

        if (user === "AnonymousUser" || user === null) {
            console.log('User not logged in');
        } else {
            updateUserOrder(productId, action);
        }
    });
}

function updateUserOrder(productId, action) {
    console.log('User logged in, adding to cart...');
    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => response.json())
        .then((data) => {
            console.log('Response Data:', data);
            location.reload();
        });
}

// Lấy CSRF token từ cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');  // Lấy CSRF token

// Lấy thông tin người dùng từ Django
var user = JSON.parse(document.getElementById('user-data').textContent);
