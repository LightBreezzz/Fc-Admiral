document.addEventListener('DOMContentLoaded', function () {
    
    const swiper = new Swiper('.news-slider', {
        loop: true,
        autoplay: {
            delay: 15000,
            disableOnInteraction: false,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
          },
        observer: true,
        observeParents: true,
    });
    
    const phoneButtons = document.querySelectorAll('.anceta__phoneBtn');
    const modal = document.getElementById('phoneModal');

    if (phoneButtons.length === 0 || !modal) return;

    const closeBtn = modal.querySelector('.modal-close');
    if (!closeBtn) return;

    // Открыть окно по клику на ЛЮБУЮ кнопку
    phoneButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            modal.style.display = 'flex';
        });
    });

    // Закрыть по крестику
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Закрыть по клику вне окна
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Закрыть по Esc
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === 'flex') {
            modal.style.display = 'none';
        }
    });

    /* Custom select for branch */
    const selectWrapper = document.getElementById('branch-select');
    if (selectWrapper) {
        const control = selectWrapper.querySelector('.select-arrow__control');
        const valueEl = selectWrapper.querySelector('.select-arrow__value');
        const menu = selectWrapper.querySelector('.select-arrow__menu');
        const options = selectWrapper.querySelectorAll('.select-arrow__option');
        const hiddenInput = document.getElementById('branch-input');

        function closeMenu() {
            menu.style.display = 'none';
            selectWrapper.setAttribute('data-open', 'false');
        }

        function openMenu() {
            menu.style.display = 'block';
            selectWrapper.setAttribute('data-open', 'true');
        }

        control.addEventListener('click', function (e) {
            e.stopPropagation();
            const isOpen = selectWrapper.getAttribute('data-open') === 'true';
            if (isOpen) {
                closeMenu();
            } else {
                openMenu();
            }
        });

        options.forEach(opt => {
            opt.addEventListener('click', function (e) {
                e.stopPropagation();
                const val = this.getAttribute('data-value');
                const text = this.textContent;

                valueEl.textContent = text;
                hiddenInput.value = val;

                closeMenu();
            });
        });

        document.addEventListener('click', function () {
            closeMenu();
        });
    }
    const hasFormErrors = document.querySelector('.anceta__field.has-error, .form-error');
    if (hasFormErrors) {
        const ancetaSection = document.getElementById('anceta');
        if (ancetaSection) {
            setTimeout(() => {
                ancetaSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
                
                // Фокус на первом поле с ошибкой
                const firstErrorField = document.querySelector(
                    '.anceta__field.has-error input, .anceta__field.has-error select'
                );
                if (firstErrorField) {
                    // Убираем outline при фокусе (если нужно)
                    firstErrorField.focus();
                }
            }, 100);
        }
    }
    const successModal = document.getElementById('successModal');
    if (successModal) {
        const successClose = successModal.querySelector('.modal-close');
        
        if (successClose) {
            successClose.addEventListener('click', () => {
                successModal.style.display = 'none';
            });
        }

        successModal.addEventListener('click', (e) => {
            if (e.target === successModal) {
                successModal.style.display = 'none';
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && successModal.style.display === 'flex') {
                successModal.style.display = 'none';
            }
        });
    }
    const phoneInput = document.querySelector('[name="parent_phone"]');
    if (phoneInput && !phoneInput.inputmask) {
        new Inputmask("+7 (999) 999-99-99", {
            showMaskOnHover: false,
            showMaskOnFocus: true
        }).mask(phoneInput);
    }
    if (window.innerWidth <= 768) {
        const placeholder = document.querySelector('.menu-burger-placeholder');
        const header = document.querySelector('header.menu'); // оригинальный хедер
    
        if (placeholder && header) {
          // Создаём бургер-кнопку
          const burger = document.createElement('button');
          burger.className = 'menu__burger';
          burger.innerHTML = '<span></span><span></span><span></span>';
          burger.setAttribute('aria-label', 'Меню');
    
          // Вставляем в placeholder
          placeholder.appendChild(burger);
    
          // Скрываем оригинальный хедер
          header.style.display = 'none';
    
          // Создаём мобильное меню
          const mobileMenu = header.cloneNode(true);
          mobileMenu.className = 'menu menu__mobile';
          mobileMenu.style.display = 'none';
          mobileMenu.style.position = 'fixed';
          mobileMenu.style.top = '0';
          mobileMenu.style.right = '-100%';
          mobileMenu.style.width = '80%';
          mobileMenu.style.maxWidth = '300px';
          mobileMenu.style.height = '100vh';
          mobileMenu.style.background = '#fff';
          mobileMenu.style.padding = '80px 20px 20px';
          mobileMenu.style.boxShadow = '-2px 0 10px rgba(0,0,0,0.1)';
          mobileMenu.style.zIndex = '1000';
          mobileMenu.style.transition = 'right 0.3s ease';
    
          // Вставляем в body
          document.body.appendChild(mobileMenu);
    
          // Обработчик
          burger.addEventListener('click', () => {
            mobileMenu.style.right = mobileMenu.style.right === '0px' ? '-100%' : '0';
          });
    
          // Закрытие при клике вне
          document.addEventListener('click', (e) => {
            if (!mobileMenu.contains(e.target) && e.target !== burger) {
              mobileMenu.style.right = '-100%';
            }
          });
        }
      }
});

/* Scroll to anceta function */
function scrollToAnceta() {
    const ancetaSection = document.getElementById('anceta');
    if (ancetaSection) {
        const elementPosition = ancetaSection.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset; // 100px отступ сверху
        
        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    }
}