document.addEventListener("DOMContentLoaded", function () {
    // 1. Обработчик для открытия/закрытия выпадающих меню
    const dropdownToggles = document.querySelectorAll('.dropdown_toggle');
    const dropdownMenus = document.querySelectorAll('.dropdown-menu');

    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function (e) {
            e.stopPropagation(); // Останавливаем всплытие события

            // Находим выпадающее меню, которое следует показать или скрыть
            const dropdownMenu = this.nextElementSibling;

            // Переключаем класс 'show', который управляет видимостью
            dropdownMenu.classList.toggle('show');

            // Переключаем атрибут aria-expanded на противоположное значение
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !isExpanded);
        });
    });

    // Закрытие всех меню при клике вне их области
    document.addEventListener('click', function (e) {
        const isClickInside = e.target.closest('.dropdown') || e.target.closest('.nav-list__item');

        if (!isClickInside) {
            // Скрываем все выпадающие меню
            dropdownMenus.forEach(menu => {
                menu.classList.remove('show');
            });

            // Сбрасываем aria-expanded
            dropdownToggles.forEach(toggle => {
                toggle.setAttribute('aria-expanded', 'false');
            });
        }
    });

    // 2. Инициализация Swiper (слайдер)
    const swiper = new Swiper('.swiper', {
        speed: 600,
        loop: true,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
            renderBullet: function (index, className) {
                return `<span class="${className}"></span>`;
            },
        },
        autoplay: {
            delay: 4000,
            disableOnInteraction: false,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
    });

    // 3. Открытие/закрытие фильтра
    document.addEventListener('click', function (event) {
        const filterButton = document.getElementById('filtersButton');
        const dropdownFilterMenu = document.querySelector('.dropdown-filter');
        if (event.target === filterButton) {
            dropdownFilterMenu.style.display = dropdownFilterMenu.style.display === 'block' ? 'none' : 'block';
        } else if (!event.target.closest('.filter')) {
            dropdownFilterMenu.style.display = 'none';
        }
    });

    // 4. Добавление в корзину
    $(document).ready(function () {
        var successMessage = $("#jq-notification");

        // Ловим событие клика по кнопке добавить в корзину
        $(document).on("click", ".add-to-cart-button", function (e) {
            e.preventDefault();

            var productsInCartCount = $(".products-in-cart-count");
            var cartCount = parseInt(productsInCartCount.text() || 0);
            var product_id = $(this).data("product-id");
            var add_to_cart_url = $(this).attr("href");

            $.ajax({
                type: "POST",
                url: add_to_cart_url,
                data: {
                    product_id: product_id,
                    csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                },
                success: function (data) {
                    successMessage.html(data.message);
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.fadeOut(400);
                    }, 7000);

                    cartCount++;
                    productsInCartCount.text(cartCount);

                    var cartItemsContainer = $("#cart-items-container");
                    cartItemsContainer.html(data.cart_items_html);
                },
                error: function () {
                    console.log("Ошибка при добавлении товара в корзину");
                },
            });
        });

        // Ловим событие клика по кнопке удалить товар из корзины
        $(document).on("click", ".remove-from-cart", function (e) {
            e.preventDefault();

            var productsInCartCount = $(".products-in-cart-count");
            var cartCount = parseInt(productsInCartCount.text() || 0);
            var cart_id = $(this).data("cart-id");
            var remove_from_cart_url = $(this).attr("href");

            $.ajax({
                type: "POST",
                url: remove_from_cart_url,
                data: {
                    cart_id: cart_id,
                    csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                },
                success: function (data) {
                    successMessage.html(data.message);
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.fadeOut(400);
                    }, 7000);

                    cartCount -= data.quantity_deleted;
                    productsInCartCount.text(cartCount);

                    var cartItemsContainer = $("#cart-items-container");
                    cartItemsContainer.html(data.cart_items_html);
                },
                error: function () {
                    console.log("Ошибка при удалении товара из корзины");
                },
            });
        });

        // Обработчик для изменения количества товара
        $(document).on("click", ".decrement, .increment", function () {
            var url = $(this).data("cart-change-url");
            var cartID = $(this).data("cart-id");
            var $input = $(this).closest('.input-group').find('.number');
            var currentValue = parseInt($input.val());

            if ($(this).hasClass('decrement') && currentValue > 1) {
                $input.val(currentValue - 1);
                updateCart(cartID, currentValue - 1, -1, url);
            } else if ($(this).hasClass('increment')) {
                $input.val(currentValue + 1);
                updateCart(cartID, currentValue + 1, 1, url);
            }
        });

        function updateCart(cartID, quantity, change, url) {
            $.ajax({
                type: "POST",
                url: url,
                data: {
                    cart_id: cartID,
                    quantity: quantity,
                    csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
                },
                success: function (data) {
                    successMessage.html(data.message);
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.fadeOut(400);
                    }, 7000);

                    var productsInCartCount = $(".products-in-cart-count");
                    var cartCount = parseInt(productsInCartCount.text() || 0);
                    cartCount += change;
                    productsInCartCount.text(cartCount);

                    var cartItemsContainer = $("#cart-items-container");
                    cartItemsContainer.html(data.cart_items_html);
                },
                error: function () {
                    console.log("Ошибка при обновлении товара в корзине");
                },
            });
        }

        // Удаляем уведомления через 7 секунд
        var notification = $('#notification');
        if (notification.length > 0) {
            setTimeout(function () {
                notification.alert('close');
            }, 7000);
        }

        // Открытие модального окна при клике на значок корзины
        $('#modalButton').click(function () {
            $('#exampleModal').appendTo('body');
            $('#exampleModal').modal('show');
        });

        // Закрытие окна корзины
        $('#exampleModal .btn-close').click(function () {
            $('#exampleModal').modal('hide');
        });

        // Обработчик события для радиокнопки выбора способа доставки
        $("input[name='requires_delivery']").change(function () {
            var selectedValue = $(this).val();
            if (selectedValue === "1") {
                $("#deliveryAddressField").show();
            } else {
                $("#deliveryAddressField").hide();
            }
        });
    });

    // Форматирование ввода номера телефона
    document.addEventListener('DOMContentLoaded', function () {
    var phoneInput = document.getElementById('id_phone_number');
    if (phoneInput) {
        phoneInput.addEventListener('input', function (e) {
            var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,2})(\d{0,2})(\d{0,2})/);
            e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '') + (x[4] ? '-' + x[4] : '');
        });
    }
});

    // Валидация номера телефона
    $('#create_order_form').on('submit', function (event) {
        var phoneNumber = $('#id_phone_number').val();
        var regex = /^\(\d{3}\) \d{2}-\d{2}-\d{2}$/;

        if (!regex.test(phoneNumber)) {
            $('#phone_number_error').show();
            event.preventDefault();
        } else {
            $('#phone_number_error').hide();
            var cleanedPhoneNumber = phoneNumber.replace(/[()\-\s]/g, '');
            $('#id_phone_number').val(cleanedPhoneNumber);
        }
    });

    // 5. Обработчик миниатюр изображений

    let thumbnails = document.getElementsByClassName('thumbnail');
    let activeImages = document.getElementsByClassName('active');

    for (let i = 0; i < thumbnails.length; i++) {
        thumbnails[i].addEventListener('mouseover', function () {

            if (activeImages.length > 0) {
                activeImages[0].classList.remove('active');
            }
            this.classList.add('active');
            document.getElementById('featured').src = this.src;
        })
    }
    let buttonLeft = document.getElementById('slideLeft');
    let buttonRight = document.getElementById('slideRight');

    buttonLeft.addEventListener('click', function(){
        document.getElementById('slider').scrollLeft -= 180
    })
    buttonRight.addEventListener('click', function(){
        document.getElementById('slider').scrollLeft += 180
    })

    // 6. Кнопка раскрытия текста
    const buttons = document.querySelectorAll('.toggle-description');
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const cardText = this.closest('.card-text');
            const shortDesc = cardText.querySelector('.short-description');
            const fullDesc = cardText.querySelector('.full-description');
            if (shortDesc.style.display === 'none') {
                shortDesc.style.display = '';
                fullDesc.style.display = 'none';
                this.textContent = 'Читать далее';
            } else {
                shortDesc.style.display = 'none';
                fullDesc.style.display = '';
                this.textContent = 'Свернуть';
            }
        });
    });


// 7. Аватарка профиля
    document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.getElementById("id_image");
    const imagePreview = document.getElementById("image-preview");

    if (imageInput && imagePreview) {
        imageInput.addEventListener("change", function (event) {
            const file = event.target.files[0];
            let previewImage = document.getElementById("preview-image");
            let noImageText = document.getElementById("no-image-text");

            if (file) {
                const reader = new FileReader();

                reader.onload = function (e) {
                    if (previewImage) {
                        previewImage.src = e.target.result;
                    } else {
                        previewImage = document.createElement('img');
                        previewImage.src = e.target.result;
                        previewImage.alt = "Profile Image";
                        previewImage.id = "preview-image";
                        previewImage.style.width = "250px";
                        previewImage.style.height = "250px";
                        previewImage.style.objectFit = "cover";

                        if (noImageText) {
                            noImageText.remove();
                        }
                        imagePreview.appendChild(previewImage);
                    }
                };

                reader.readAsDataURL(file);
            } else {
                if (previewImage) {
                    previewImage.remove();
                }
                if (!noImageText) {
                    noImageText = document.createElement('p');
                    noImageText.id = "no-image-text";
                    noImageText.textContent = "No image uploaded";
                    imagePreview.appendChild(noImageText);
                }
            }
        });
    } else {
        console.error("Элемент с id 'id_image' или 'image-preview' не найден!");
    }
});

});
