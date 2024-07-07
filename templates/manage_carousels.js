// static/js/manage_carousels.js
$(document).ready(function () {
    const carouselList = $('#carouselList');

    function fetchCarouselItems() {
        $.ajax({
            url: '/api/carousel-items',
            method: 'GET',
            success: function (data) {
                carouselList.empty();
                data.forEach(function (item, index) {
                    carouselList.append(`
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                            <span>${item.alt_text} - ${item.image_url}</span>
                            <button class="btn btn-danger btn-sm" onclick="deleteCarouselItem(${index})">Delete</button>
                        </li>
                    `);
                });
            },
            error: function (error) {
                console.error('Error fetching carousel items:', error);
            }
        });
    }

    $('#carouselForm').on('submit', function (event) {
        event.preventDefault();
        const imageUrl = $('#imageUrl').val();
        const altText = $('#altText').val();

        $.ajax({
            url: '/api/carousel-items',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ image_url: imageUrl, alt_text: altText }),
            success: function () {
                fetchCarouselItems();
                $('#carouselForm')[0].reset();
            },
            error: function (error) {
                console.error('Error adding carousel item:', error);
            }
        });
    });

    window.deleteCarouselItem = function (index) {
        $.ajax({
            url: `/api/carousel-items/${index}`,
            method: 'DELETE',
            success: function () {
                fetchCarouselItems();
            },
            error: function (error) {
                console.error('Error deleting carousel item:', error);
            }
        });
    };

    fetchCarouselItems();
});
