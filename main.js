// main.js

$(document).ready(function() {
    // Initialize the carousel
    $('#productCarousel').carousel({
        interval: 3000 // Change slide every 3 seconds
    });

    // Handle previous/next controls
    $('.carousel-control-prev').click(function() {
        $('#productCarousel').carousel('prev');
    });

    $('.carousel-control-next').click(function() {
        $('#productCarousel').carousel('next');
    });

    // Example function to dynamically load carousel items
    function loadCarouselItems() {
        $.ajax({
            url: '/api/carousel-items',
            method: 'GET',
            success: function(data) {
                var indicators = '';
                var items = '';
                data.forEach(function(item, index) {
                    indicators += `<li data-target="#productCarousel" data-slide-to="${index}" ${index === 0 ? 'class="active"' : ''}></li>`;
                    items += `
                        <div class="carousel-item ${index === 0 ? 'active' : ''}">
                            <img class="d-block w-100" src="${item.image_url}" alt="${item.alt_text}">
                            <div class="carousel-caption d-none d-md-block">
                                <h5>${item.title}</h5>
                                <p>${item.description}</p>
                            </div>
                        </div>`;
                });
                $('.carousel-indicators').html(indicators);
                $('.carousel-inner').html(items);
            },
            error: function(error) {
                console.error('Error fetching carousel items:', error);
            }
        });
    }

    // Load carousel items on page load
    loadCarouselItems();
});

