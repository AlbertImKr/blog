/**
 * Blogzine - Blog and Magazine Bootstrap 5 Theme
 *
 * @author Webestica (https://www.webestica.com/)
 * @version 1.3.2
 **/

/* ===================
Table Of Content
======================
01 PRELOADER
02 MEGA MENU
03 STICKY HEADER
04 TINY SLIDER
05 PARALLAX BACKGROUND
06 STICKY BAR
07 TOOLTIP
08 POPOVER
09 BACK TO TOP
10 STICKY POST
11 STICKY FOOTER
12 GLIGHTBOX
13 ISOTOPE
14 FONT SIZE
15 LAZY LOAD
16 QUILL EDITOR
17 VIDEO PLAYER
18 OVERLAY SCROLLBAR
19 DASHBOARD CHART
20 TRAFFIC CHART
21 RENDER DELTA USE QUILL
22 AJAX POSTS FRAGMENT LOADING
23 AJAX DELETE POST
24 AJAX SORT POSTS
25 AJAX MORE POST LOADING
26 UPLOAD IMAGE
27 DELETE IMAGE
====================== */

"use strict";
!function () {

    window.Element.prototype.removeClass = function () {
        let className = arguments.length > 0 && void 0 !== arguments[0]
                ? arguments[0] : "",
            selectors = this;
        if (!(selectors instanceof HTMLElement) && selectors !== null) {
            selectors = document.querySelector(selectors);
        }
        if (this.isVariableDefined(selectors) && className) {
            selectors.classList.remove(className);
        }
        return this;
    }, window.Element.prototype.addClass = function () {
        let className = arguments.length > 0 && void 0 !== arguments[0]
                ? arguments[0] : "",
            selectors = this;
        if (!(selectors instanceof HTMLElement) && selectors !== null) {
            selectors = document.querySelector(selectors);
        }
        if (this.isVariableDefined(selectors) && className) {
            selectors.classList.add(className);
        }
        return this;
    }, window.Element.prototype.toggleClass = function () {
        let className = arguments.length > 0 && void 0 !== arguments[0]
                ? arguments[0] : "",
            selectors = this;
        if (!(selectors instanceof HTMLElement) && selectors !== null) {
            selectors = document.querySelector(selectors);
        }
        if (this.isVariableDefined(selectors) && className) {
            selectors.classList.toggle(className);
        }
        return this;
    }, window.Element.prototype.isVariableDefined = function () {
        return !!this && typeof (this) != 'undefined' && this != null;
    }
}();

// Get CSS var value
var ThemeColor = function () {
    return {
        getCssVariableValue: function (e) {
            var t = getComputedStyle(document.documentElement).getPropertyValue(
                e);
            return t && t.length > 0 && (t = t.trim()), t;
        }
    };
}();

var e = {
    init: function () {
        e.preLoader(),
            e.megaMenu(),
            e.stickyHeader(),
            e.tinySlider(),
            e.parallaxBG(),
            e.stickyBar(),
            e.toolTipFunc(),
            e.popOverFunc(),
            e.backTotop(),
            e.stickyPost(),
            e.stickyFooter(),
            e.lightBox(),
            e.enableIsotope(),
            e.zooming(),
            e.lazyLoading(),
            e.quill(),
            e.videoPlyr(),
            e.overlayScrollbars(),
            e.trafficsourcesChart(),
            e.trafficstatsChart(),
            e.renderDeltaUseQuill(),
            e.ajaxPostsFragmentLoading(),
            e.ajaxSortPosts(),
            e.uploadImage(),
            e.deleteImage(),
            e.ajaxMorePostLoading();
    },
    isVariableDefined: function (el) {
        return typeof !!el && (el) != 'undefined' && el != null;
    },
    getParents: function (el, selector, filter) {
        const result = [];
        const matchesSelector = el.matches || el.webkitMatchesSelector
            || el.mozMatchesSelector || el.msMatchesSelector;

        // match start from parent
        el = el.parentElement;
        while (el && !matchesSelector.call(el, selector)) {
            if (!filter) {
                if (selector) {
                    if (matchesSelector.call(el, selector)) {
                        return result.push(el);
                    }
                } else {
                    result.push(el);
                }
            } else {
                if (matchesSelector.call(el, filter)) {
                    result.push(el);
                }
            }
            el = el.parentElement;
            if (e.isVariableDefined(el)) {
                if (matchesSelector.call(el, selector)) {
                    return el;
                }
            }

        }
        return result;
    },
    getNextSiblings: function (el, selector, filter) {
        let sibs = [];
        let nextElem = el.parentNode.firstChild;
        const matchesSelector = el.matches || el.webkitMatchesSelector
            || el.mozMatchesSelector || el.msMatchesSelector;
        do {
            if (nextElem.nodeType === 3) {
                continue;
            } // ignore text nodes
            if (nextElem === el) {
                continue;
            } // ignore elem of target
            if (nextElem === el.nextElementSibling) {
                if ((!filter || filter(el))) {
                    if (selector) {
                        if (matchesSelector.call(nextElem, selector)) {
                            return nextElem;
                        }
                    } else {
                        sibs.push(nextElem);
                    }
                    el = nextElem;

                }
            }
        } while (nextElem = nextElem.nextSibling)
        return sibs;
    },
    on: function (selectors, type, listener) {
        document.addEventListener("DOMContentLoaded", () => {
            if (!(selectors instanceof HTMLElement) && selectors !== null) {
                selectors = document.querySelector(selectors);
            }
            selectors.addEventListener(type, listener);
        });
    },
    onAll: function (selectors, type, listener) {
        document.addEventListener("DOMContentLoaded", () => {
            document.querySelectorAll(selectors).forEach((element) => {
                if (type.indexOf(',') > -1) {
                    let types = type.split(',');
                    types.forEach((type) => {
                        element.addEventListener(type, listener);
                    });
                } else {
                    element.addEventListener(type, listener);
                }

            });
        });
    },
    removeClass: function (selectors, className) {
        if (!(selectors instanceof HTMLElement) && selectors !== null) {
            selectors = document.querySelector(selectors);
        }
        if (e.isVariableDefined(selectors)) {
            selectors.removeClass(className);
        }
    },
    removeAllClass: function (selectors, className) {
        if (e.isVariableDefined(selectors) && (selectors
            instanceof HTMLElement)) {
            document.querySelectorAll(selectors).forEach((element) => {
                element.removeClass(className);
            });
        }

    },
    toggleClass: function (selectors, className) {
        if (!(selectors instanceof HTMLElement) && selectors !== null) {
            selectors = document.querySelector(selectors);
        }
        if (e.isVariableDefined(selectors)) {
            selectors.toggleClass(className);
        }
    },
    toggleAllClass: function (selectors, className) {
        if (e.isVariableDefined(selectors) && (selectors
            instanceof HTMLElement)) {
            document.querySelectorAll(selectors).forEach((element) => {
                element.toggleClass(className);
            });
        }
    },
    addClass: function (selectors, className) {
        if (!(selectors instanceof HTMLElement) && selectors !== null) {
            selectors = document.querySelector(selectors);
        }
        if (e.isVariableDefined(selectors)) {
            selectors.addClass(className);
        }
    },
    select: function (selectors) {
        return document.querySelector(selectors);
    },
    selectAll: function (selectors) {
        return document.querySelectorAll(selectors);
    },

    // START: 01 Preloader
    preLoader: function () {
        window.onload = function () {
            var preloader = e.select('.preloader');
            if (e.isVariableDefined(preloader)) {
                preloader.className += ' animate__animated animate__fadeOut';
                setTimeout(function () {
                    preloader.style.display = 'none';
                }, 200);
            }
        };
    },
    // END: Preloader

    // START: 02 Mega Menu
    megaMenu: function () {
        e.onAll('.dropdown-menu a.dropdown-item.dropdown-toggle', 'click',
            function (event) {
                var element = this;
                event.preventDefault();
                event.stopImmediatePropagation();
                if (e.isVariableDefined(element.nextElementSibling)
                    && !element.nextElementSibling.classList.contains("show")) {
                    const parents = e.getParents(element, '.dropdown-menu');
                    e.removeClass(parents.querySelector('.show'), "show");
                    if (e.isVariableDefined(
                        parents.querySelector('.dropdown-opened'))) {
                        e.removeClass(parents.querySelector('.dropdown-opened'),
                            "dropdown-opened");
                    }

                }
                var $subMenu = e.getNextSiblings(element, ".dropdown-menu");
                e.toggleClass($subMenu, "show");
                $subMenu.previousElementSibling.toggleClass('dropdown-opened');
                var parents = e.getParents(element,
                    'li.nav-item.dropdown.show');
                if (e.isVariableDefined(parents) && parents.length > 0) {
                    e.on(parents, 'hidden.bs.dropdown', function (event) {
                        e.removeAllClass('.dropdown-submenu .show');
                    });
                }
            });
    },
    // END: Mega Menu

    // START: 03 Sticky Header
    stickyHeader: function () {
        var stickyNav = e.select('.navbar-sticky');
        if (e.isVariableDefined(stickyNav)) {
            var stickyHeight = stickyNav.offsetHeight;
            stickyNav.insertAdjacentHTML('afterend',
                '<div id="sticky-space"></div>');
            var stickySpace = e.select('#sticky-space');
            if (e.isVariableDefined(stickySpace)) {
                document.addEventListener('scroll', function (event) {
                    var scTop = window.pageYOffset
                        || document.documentElement.scrollTop;
                    if (scTop >= 400) {
                        stickySpace.addClass('active');
                        e.select(
                            "#sticky-space.active").style.height = stickyHeight
                            + 'px';
                        stickyNav.addClass('navbar-sticky-on');
                    } else {
                        stickySpace.removeClass('active');
                        stickySpace.style.height = '0px';
                        stickyNav.removeClass("navbar-sticky-on");
                    }
                });
            }
        }
    },
    // END: Sticky Header

    // START: 04 Tiny Slider
    tinySlider: function () {
        var $carousel = e.select('.tiny-slider-inner');
        if (e.isVariableDefined($carousel)) {
            var tnsCarousel = e.selectAll('.tiny-slider-inner');
            tnsCarousel.forEach(slider => {
                var slider1 = slider;
                var sliderMode = slider1.getAttribute('data-mode')
                    ? slider1.getAttribute('data-mode') : 'carousel';
                var sliderAxis = slider1.getAttribute('data-axis')
                    ? slider1.getAttribute('data-axis') : 'horizontal';
                var sliderSpace = slider1.getAttribute('data-gutter')
                    ? slider1.getAttribute('data-gutter') : 30;
                var sliderEdge = slider1.getAttribute('data-edge')
                    ? slider1.getAttribute('data-edge') : 0;

                var sliderItems = slider1.getAttribute('data-items')
                    ? slider1.getAttribute('data-items') : 4; //option: number (items in all device)
                var sliderItemsXl = slider1.getAttribute('data-items-xl')
                    ? slider1.getAttribute('data-items-xl') : Number(
                        sliderItems); //option: number (items in 1200 to end )
                var sliderItemsLg = slider1.getAttribute('data-items-lg')
                    ? slider1.getAttribute('data-items-lg') : Number(
                        sliderItemsXl); //option: number (items in 992 to 1199 )
                var sliderItemsMd = slider1.getAttribute('data-items-md')
                    ? slider1.getAttribute('data-items-md') : Number(
                        sliderItemsLg); //option: number (items in 768 to 991 )
                var sliderItemsSm = slider1.getAttribute('data-items-sm')
                    ? slider1.getAttribute('data-items-sm') : Number(
                        sliderItemsMd); //option: number (items in 576 to 767 )
                var sliderItemsXs = slider1.getAttribute('data-items-xs')
                    ? slider1.getAttribute('data-items-xs') : Number(
                        sliderItemsSm); //option: number (items in start to 575 )

                var sliderSpeed = slider1.getAttribute('data-speed')
                    ? slider1.getAttribute('data-speed') : 500;
                var sliderautoWidth = slider1.getAttribute('data-autowidth')
                    === 'true'; //option: true or false
                var sliderArrow = slider1.getAttribute('data-arrow')
                    !== 'false'; //option: true or false
                var sliderDots = slider1.getAttribute('data-dots') !== 'false'; //option: true or false

                var sliderAutoPlay = slider1.getAttribute('data-autoplay')
                    !== 'false'; //option: true or false
                var sliderAutoPlayTime = slider1.getAttribute(
                    'data-autoplaytime') ? slider1.getAttribute(
                    'data-autoplaytime') : 4000;
                var sliderHoverPause = slider1.getAttribute('data-hoverpause')
                    === 'true'; //option: true or false
                if (e.isVariableDefined(e.select('.custom-thumb'))) {
                    var sliderNavContainer = e.select('.custom-thumb');
                }
                var sliderLoop = slider1.getAttribute('data-loop') !== 'false'; //option: true or false
                var sliderRewind = slider1.getAttribute('data-rewind')
                    === 'true'; //option: true or false
                var sliderAutoHeight = slider1.getAttribute('data-autoheight')
                    === 'true'; //option: true or false
                var sliderfixedWidth = slider1.getAttribute('data-fixedwidth')
                    === 'true'; //option: true or false
                var sliderTouch = slider1.getAttribute('data-touch')
                    !== 'false'; //option: true or false
                var sliderDrag = slider1.getAttribute('data-drag') !== 'false'; //option: true or false
                // Check if document DIR is RTL
                var ifRtl = document.getElementsByTagName(
                    "html")[0].getAttribute("dir");
                var sliderDirection;
                if (ifRtl === 'rtl') {
                    sliderDirection = 'rtl';
                }

                var tnsSlider = tns({
                    container: slider,
                    mode: sliderMode,
                    axis: sliderAxis,
                    gutter: sliderSpace,
                    edgePadding: sliderEdge,
                    speed: sliderSpeed,
                    autoWidth: sliderautoWidth,
                    controls: sliderArrow,
                    nav: sliderDots,
                    autoplay: sliderAutoPlay,
                    autoplayTimeout: sliderAutoPlayTime,
                    autoplayHoverPause: sliderHoverPause,
                    autoplayButton: false,
                    autoplayButtonOutput: false,
                    controlsPosition: top,
                    navContainer: sliderNavContainer,
                    navPosition: top,
                    autoplayPosition: top,
                    controlsText: [
                        '<i class="fas fa-chevron-left"></i>',
                        '<i class="fas fa-chevron-right"></i>'
                    ],
                    loop: sliderLoop,
                    rewind: sliderRewind,
                    autoHeight: sliderAutoHeight,
                    fixedWidth: sliderfixedWidth,
                    touch: sliderTouch,
                    mouseDrag: sliderDrag,
                    arrowKeys: true,
                    items: sliderItems,
                    textDirection: sliderDirection,
                    lazyload: true,
                    lazyloadSelector: '.lazy',
                    responsive: {
                        0: {
                            items: Number(sliderItemsXs)
                        },
                        576: {
                            items: Number(sliderItemsSm)
                        },
                        768: {
                            items: Number(sliderItemsMd)
                        },
                        992: {
                            items: Number(sliderItemsLg)
                        },
                        1200: {
                            items: Number(sliderItemsXl)
                        }
                    }
                });
            });
        }
    },
    // END: Tiny Slider

    // START: 05 Parallax Background
    parallaxBG: function () {
        var parBG = e.select('.bg-parallax');
        if (e.isVariableDefined(parBG)) {
            jarallax(e.selectAll('.bg-parallax'), {
                speed: 0.6
            });
        }
    },
    // END: Parallax Background

    // START: 06 Sticky Bar
    stickyBar: function () {
        var sb = e.select('[data-sticky]');
        if (e.isVariableDefined(sb)) {
            var sticky = new Sticky('[data-sticky]');
        }
    },
    // END: Sticky Bar

    // START: 07 Tooltip
    // Enable tooltips everywhere via data-toggle attribute
    toolTipFunc: function () {
        var tooltipTriggerList = [].slice.call(
            e.selectAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl)
        })
    },
    // END: Tooltip

    // START: 08 Popover
    // Enable popover everywhere via data-toggle attribute
    popOverFunc: function () {
        var popoverTriggerList = [].slice.call(
            e.selectAll('[data-bs-toggle="popover"]'))
        var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
            return new bootstrap.Popover(popoverTriggerEl)
        })
    },
    // END: Popover

    // START: 09 Back to Top
    backTotop: function () {
        var scrollpos = window.scrollY;
        var backBtn = e.select('.back-top');
        if (e.isVariableDefined(backBtn)) {
            var add_class_on_scroll = () => backBtn.addClass("back-top-show");
            var remove_class_on_scroll = () => backBtn.removeClass(
                "back-top-show");

            window.addEventListener('scroll', function () {
                scrollpos = window.scrollY;
                if (scrollpos >= 800) {
                    add_class_on_scroll()
                } else {
                    remove_class_on_scroll()
                }
            });

            backBtn.addEventListener('click', () => window.scrollTo({
                top: 0,
                behavior: 'smooth',
            }));
        }
    },
    // END: Back to Top

    // START: 10 Sticky post
    stickyPost: function () {
        var scrollpos = window.scrollY;
        var sp = e.select('.sticky-post');
        if (e.isVariableDefined(sp)) {
            var add_class_on_scroll = () => sp.addClass("sticky-post-sticked");
            var remove_class_on_scroll = () => sp.removeClass(
                "sticky-post-sticked");

            window.addEventListener('scroll', function () {
                scrollpos = window.scrollY;
                if (scrollpos >= 1400) {
                    add_class_on_scroll()
                } else {
                    remove_class_on_scroll()
                }
            });
        }
    },
    // END: Sticky Post

    // START: 11 Sticky Footer
    stickyFooter: function () {
        var fixedFooter = e.select('.footer-sticky');
        if (e.isVariableDefined(fixedFooter)) {
            window.addEventListener("load", function () {
                window.dispatchEvent(new Event('resize'));
            });
            window.addEventListener('resize', function (event) {
                var screenWidth = window.outerWidth;
                var footerHeight = fixedFooter.offsetHeight - 1;
                if (screenWidth >= 768) {
                    document.getElementsByTagName(
                        'main')[0].style.marginBottom = footerHeight + 'px';
                }
            });
        }
    },
    // END: Sticky Footer

    // START: 12 GLightbox
    lightBox: function () {
        var light = e.select('[data-glightbox]');
        if (e.isVariableDefined(light)) {
            var lb = GLightbox({
                selector: '*[data-glightbox]',
                openEffect: 'fade',
                closeEffect: 'fade'
            });
        }
    },
    // END: GLightbox

    // START: 13 Isotope
    enableIsotope: function () {
        var isGridItem = e.select('.grid-item');
        if (e.isVariableDefined(isGridItem)) {

            // Code only for normal Grid
            var onlyGrid = e.select('[data-isotope]');
            if (e.isVariableDefined(onlyGrid)) {
                var allGrid = e.selectAll("[data-isotope]");
                allGrid.forEach(gridItem => {
                    var gridItemData = gridItem.getAttribute('data-isotope');
                    var gridItemDataObj = JSON.parse(gridItemData);
                    var iso = new Isotope(gridItem, {
                        itemSelector: '.grid-item',
                        layoutMode: gridItemDataObj.layoutMode
                    });

                    imagesLoaded(gridItem).on('progress', function () {
                        // layout Isotope after each image loads
                        iso.layout();
                    });
                });
            }

            // Code only for normal Grid
            var onlyGridFilter = e.select('.grid-menu');
            if (e.isVariableDefined(onlyGridFilter)) {
                var filterMenu = e.selectAll('.grid-menu');
                filterMenu.forEach(menu => {
                    var filterContainer = menu.getAttribute('data-target');
                    var a = menu.dataset.target;
                    var b = e.select(a);
                    var filterContainerItemData = b.getAttribute(
                        'data-isotope');
                    var filterContainerItemDataObj = JSON.parse(
                        filterContainerItemData);
                    var filter = new Isotope(filterContainer, {
                        itemSelector: '.grid-item',
                        transitionDuration: '0.7s',
                        layoutMode: filterContainerItemDataObj.layoutMode
                    });

                    var menuItems = menu.querySelectorAll('li a');
                    menuItems.forEach(menuItem => {
                        menuItem.addEventListener('click', function (event) {
                            var filterValue = menuItem.getAttribute(
                                'data-filter');
                            filter.arrange({filter: filterValue});
                            menuItems.forEach(
                                (control) => control.removeClass('active'));
                            menuItem.addClass('active');
                        });
                    });

                    imagesLoaded(filterContainer).on('progress', function () {
                        filter.layout();
                    });
                });
            }

        }
    },
    // END: Isotope

    // START: 14 Font size
    zooming: function () {
        const doc = document.documentElement;
        var radios = document.querySelectorAll(
            'input[type=radio][name="fntradio"]');
        radios.forEach(radio => {
            radio.addEventListener("change", function () {
                var idZ = radio.getAttribute('id');
                if (idZ == 'font-sm') {
                    doc.classList.remove('font-lg');
                    doc.classList.add('font-sm');
                } else if (idZ == 'font-default') {
                    doc.classList.remove('font-sm', 'font-lg');
                } else if (idZ == 'font-lg') {
                    doc.classList.remove('font-sm');
                    doc.classList.add('font-lg');
                }
            });
        });
    },
    // END: Font size

    // START: 15 Lazy Load
    lazyLoading: function () {
        var lazLoad = e.select('.lazy');
        if (e.isVariableDefined(lazLoad)) {
            var lazyLoadInstance = new LazyLoad({});
        }
    },
    // END: Lazy Load

    // START: 16 Quill Editor
    quill: function () {
        var ql = e.select('#quilleditor');
        if (e.isVariableDefined(ql)) {
            var editor = new Quill('#quilleditor', {
                modules: {toolbar: '#quilltoolbar'},
                theme: 'snow'
            });
            const quillContent = document.getElementById('quill-content');
            if (quillContent.textContent) {
                editor.setContents(JSON.parse(quillContent.textContent));
            }
            editor.on('text-change', function (delta, oldDelta, source) {
                const contentDelta = editor.getContents();
                quillContent.textContent = JSON.stringify(contentDelta);
            });
        }
    },
    // END: Quill Editor

    // START: 17 Video player
    videoPlyr: function () {
        var vdp = e.select('.player-wrapper');
        if (e.isVariableDefined(vdp)) {
            // youtube
            const playerYoutube = Plyr.setup('.player-youtube', {});
            window.player = playerYoutube;

            // Vimeo
            const playerVimeo = Plyr.setup('.player-vimeo', {});
            window.player = playerVimeo;

            // HTML video
            const playerHtmlvideo = Plyr.setup('.player-html', {
                captions: {active: true}
            });
            window.player = playerHtmlvideo;

            // HTML audio
            const playerHtmlaudio = Plyr.setup('.player-audio', {});
            window.player = playerHtmlaudio;
        }
    },
    // END: Video player

    // START: 18 Overlay scrollbar
    overlayScrollbars: function () {
        var os = e.select('.custom-scrollbar');
        if (os) {
            document.addEventListener("DOMContentLoaded", function () {
                var cs = document.querySelectorAll('.custom-scrollbar');
                cs.forEach(c => {
                    OverlayScrollbars(c, {
                        scrollbars: {
                            autoHide: 'leave',
                            autoHideDelay: 200
                        },
                        overflowBehavior: {
                            x: "visible-hidden",
                            y: "scroll"
                        }
                    });
                });
            });
        }
    },
    // END: Overlay scrollbar

    // START: 19 Dashboard Chart
    trafficsourcesChart: function () {
        var ac = e.select('#apexChartTrafficSources');
        if (e.isVariableDefined(ac)) {
            var options = {
                colors: [
                    '#2163e8', '#0cbc87', '#d6293e', '#f7c32e'
                ],
                labels: ['Search', 'Direct', 'Social', 'Display ads'],
                series: [44, 55, 41, 17],
                legend: {
                    show: false,
                    position: 'right'
                },
                chart: {
                    height: 300,
                    type: 'donut',
                },
                plotOptions: {
                    pie: {
                        donut: {
                            size: '75%',
                        },
                        offsetY: 20,
                    },
                    stroke: {
                        colors: undefined
                    }
                },
                stroke: {
                    show: false
                },
                dataLabels: {
                    enabled: false
                },
                responsive: [{
                    breakpoint: 480,
                    options: {
                        chart: {
                            height: 200
                        },
                        legend: {
                            show: false
                        }
                    }
                }]
            };
            var chart = new ApexCharts(
                document.querySelector("#apexChartTrafficSources"), options);
            chart.render();
        }
    },
    // END: Dashboard Chart

    // START: 20 Traffic Chart
    trafficstatsChart: function () {
        var cpv = e.select('#apexChartTrafficStats');
        if (e.isVariableDefined(cpv)) {
            var options = {
                colors: [
                    '#2163e8',
                ],
                series: [{
                    name: 'Users',
                    data: [100, 401, 305, 501, 409, 602, 609, 901, 848, 602,
                        809, 901]
                }],
                chart: {
                    height: 320,
                    type: 'area',
                    toolbar: {
                        show: false
                    }
                },
                grid: {
                    strokeDashArray: 4,
                    position: 'back'
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    curve: 'smooth'
                },
                legend: {
                    show: true,
                    horizontalAlign: 'right',
                    position: 'top',
                    labels: {},
                    markers: {
                        width: 8,
                        height: 8
                    }
                },
                xaxis: {
                    labels: {
                        show: true
                    },
                    axisBorder: {
                        show: false
                    },
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                },
                tooltip: {
                    x: {
                        format: 'dd/MM/yy HH:mm'
                    },
                },
            };
            var chart = new ApexCharts(
                document.querySelector("#apexChartTrafficStats"), options);
            chart.render();
        }
    },
    // END: Traffic Chart
    // START: 21 Render Delta Use Quill
    renderDeltaUseQuill: function () {
        const deltaContent = document.getElementById('delta-content');
        const deltaData = document.getElementById('delta-data');
        if (deltaContent && deltaData) {
            const quill = new Quill('#delta-content', {
                theme: 'snow',
                readOnly: true,
                modules: {
                    toolbar: false
                }
            });
            var deltaJson = JSON.parse(deltaData.textContent);
            quill.setContents(deltaJson);
        }
    },
    // END: Render Delta Use Quill
    // START: 22 AJAX POSTS FRAGMENT LOADING
    ajaxPostsFragmentLoading: function () {
        const ajaxLinks = e.selectAll('.ajax-link');
        if (e.isVariableDefined(ajaxLinks)) {
            ajaxLinks.forEach(link => {

                let target = link.getAttribute('data-target');
                let container = e.select(target);
                if (!e.isVariableDefined(container)) {
                    return;
                }
                link.addEventListener('click', function (event) {
                    event.preventDefault();

                    let url = link.getAttribute('href');
                    let page = url.split('page=')[1];
                    let currentParams = new URLSearchParams(
                        window.location.search);
                    let windowPath = window.location.pathname;

                    if (currentParams.toString()) {
                        if (currentParams.toString().includes('page')) {
                            currentParams.delete('page');
                            windowPath += `?page=${page}`;
                        }
                        if (currentParams.toString()) {
                            url += `&${currentParams.toString()}`;
                            windowPath += `&${currentParams.toString()}`;
                        }
                    } else {
                        windowPath += `?page=${page}`;
                    }
                    window.history.pushState({}, '', windowPath);

                    fetch(url).then(response => {
                        return response.text();
                    }).then(data => {
                        let isExistParam = url.indexOf('?');
                        if (isExistParam > -1) {
                            let urlParams = url.slice(isExistParam + 1)
                            let currentParams = new URLSearchParams(
                                window.location.search);
                            if (urlParams.indexOf("&") > -1) {
                                urlParams.split('&').forEach(param => {
                                    let [key, value] = param.split('=');
                                    value = value.replace(/\+/g, ' ');
                                    currentParams.set(key, value);
                                });
                            } else {
                                let [key, value] = urlParams.split('=');
                                value = value.replace(/\+/g, ' ');
                                currentParams.set(key, value);
                            }
                        }
                        container.innerHTML = data;
                        e.ajaxPostsFragmentLoading();
                        e.ajaxSortPosts()
                    })
                    .catch(error => {
                        console.error(error)
                    });
                }.bind(this));

            });
        }
    },
    // END: AJAX POSTS FRAGMENT LOADING
    // START: 24 AJAX SORT POSTS
    ajaxSortPosts: function () {
        const sortSelect = e.select('.sort-select');
        if (e.isVariableDefined(sortSelect)) {
            let target = sortSelect.getAttribute('data-target');
            let container = e.select(target);
            if (!e.isVariableDefined(container)) {
                return;
            }
            sortSelect.addEventListener('change', function (event) {
                event.preventDefault();
                let url = sortSelect.getAttribute('data-link');
                let currentParams = new URLSearchParams(window.location.search);
                let sortValue = sortSelect.value;
                if (currentParams.toString()) {
                    if (currentParams.toString().includes('sort')) {
                        currentParams.delete('sort');
                    }
                    if (currentParams.toString()) {
                        url += `?${currentParams.toString()}`;
                    }
                }
                if (currentParams.toString()) {
                    url += `&sort=${sortValue}`;
                } else {
                    url += `?sort=${sortValue}`;
                }
                window.location.href = url;
            });
        }
    },
    // END: AJAX SORT POSTS
    // START: 25 AJAX MORE POST LOADING
    ajaxMorePostLoading: function () {
        const morePosts = e.select('.more-posts');
        const container = document.getElementById('more-button')
        if (e.isVariableDefined(morePosts) && e.isVariableDefined(container)) {
            morePosts.addEventListener('click', function (event) {
                event.preventDefault();
                const url = morePosts.getAttribute('href');
                fetch(url).then(response => {
                    return response.text();
                }).then(data => {
                    container.insertAdjacentHTML('beforebegin', data);
                    container.remove();
                    e.ajaxMorePostLoading();
                }).catch(error => {
                    console.error(error);
                });
            });
        }
    },
    // END: AJAX MORE POST LOADING
    // START: 26 UPLOAD IMAGE
    uploadImage: function () {
        const uploadImage = e.select('.upload-image');
        if (e.isVariableDefined(uploadImage)) {
            uploadImage.addEventListener('change', function (event) {
                let files = uploadImage.files
                if (files.length === 0) {
                    console.error('No file selected');
                    return;
                }
                if (files.length > 1) {
                    console.error('Only one file can be uploaded');
                    return;
                }
                let image = files[0];

                let fileTypes = ['image/jpeg', 'image/png', 'image/jpg'];
                if (fileTypes.indexOf(image.type) === -1) {
                    console.error('File type not supported');
                    return;
                }

                let url = uploadImage.getAttribute('data-url');
                url += `?file_name=${encodeURIComponent(
                    image.name)}&file_type=${encodeURIComponent(
                    image.type)}&file_size=${image.size}`;
                // 1. Signed URL 요청
                fetch(url, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                    },
                }).then(response => {
                    return response.json();
                }).then(response => {
                    if (response.error) {
                        console.error(response.error);
                        return;
                    }
                    // 2. Signed URL로 파일 업로드
                    return fetch(response.url, {
                        method: 'PUT',
                        body: image,
                        mode: 'cors',
                    })
                }).then(
                    response => {
                        if (response.ok) {
                            return response.url
                        }
                        console.error('Network response was not ok.');
                    }
                ).then(url => {
                    // 3. 이미지 URL을 서버에 보내서 이미지 생성 요청
                    let uploadUrl = uploadImage.getAttribute('data-upload-url');
                    let csrfToken = uploadImage.getAttribute('data-csrf-token');
                    if (!url) {
                        return;
                    }
                    if (url.indexOf('?') > -1) {
                        url = url.split('?')[0];
                    }
                    document.getElementById('image-preview-div').classList.remove('d-none');
                    document.getElementById('image-preview').src = url;
                    document.getElementById('image-div').classList.remove('col-sm-12', 'col-md-12');
                    document.getElementById('image-div').classList.add('col-sm-8', 'col-md-10');

                    return fetch(uploadUrl, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json',
                            'X-CSRFToken': csrfToken,
                        },
                        body: JSON.stringify({url: url}),
                    })
                })
                .then(response => response.json())
                .then(data => {
                    const imageId = data.image_id;
                    const target = document.getElementById(
                        uploadImage.getAttribute("data-target"));
                    target.value = imageId;


                })
                .catch(error => {
                    console.error(error);
                });
            }, false);
        }
    },
    // END: UPLOAD IMAGE
    // START: 27 DELETE IMAGE
    deleteImage: function () {
        const deleteButton = e.select('#delete-image-button');
        if (e.isVariableDefined(deleteButton)) {
            deleteButton.addEventListener('click', function (event) {
                event.preventDefault();
                const target = e.select(deleteButton.getAttribute('data-target'));
                if (target) {
                    target.value = '';
                }
                document.getElementById('image-preview-div').classList.add('d-none');
                document.getElementById('image-preview').src = '';
                document.getElementById('image-div').classList.remove('col-sm-8', 'col-md-10');
                document.getElementById('image-div').classList.add('col-sm-12', 'col-md-12');
            });
        }
    },
    // END: DELETE IMAGE
};
e.init();

