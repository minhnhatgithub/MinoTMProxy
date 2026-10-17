(function() {
    var THEME_KEY = 'minotm_theme';
    var docEl = document.documentElement;

    function setVisualTheme(isLight) {
        if (isLight) {
            docEl.setAttribute('data-theme', 'light');
            docEl.classList.add('theme-light');
            if (document.body) {
                document.body.setAttribute('data-theme', 'light');
                document.body.classList.add('theme-light');
            }
        } else {
            docEl.setAttribute('data-theme', 'cyber');
            docEl.classList.remove('theme-light');
            if (document.body) {
                document.body.setAttribute('data-theme', 'cyber');
                document.body.classList.remove('theme-light');
            }
        }
        var label = document.getElementById('theme-name');
        if (label) {
            label.textContent = isLight ? 'LIGHT' : 'CYBER';
        }
        try {
            localStorage.setItem(THEME_KEY, isLight ? 'light' : 'cyber');
        } catch(e) {}
    }

    window.setVisualTheme = setVisualTheme;

    window.toggleMinotmTheme = function(e) {
        if (e && e.preventDefault) e.preventDefault();
        if (e && e.stopPropagation) e.stopPropagation();
        var isCurrentLight = docEl.getAttribute('data-theme') === 'light' || docEl.classList.contains('theme-light');
        setVisualTheme(!isCurrentLight);
    };

    window.resumeAllFlows = function(e) {
        if (e && e.preventDefault) e.preventDefault();
        var nativeResume = document.querySelector('button[title*="accept all"], header .fa-forward');
        if (nativeResume) {
            (nativeResume.closest('button') || nativeResume).click();
        } else {
            window.dispatchEvent(new KeyboardEvent('keydown', { key: 'a', bubbles: true }));
        }
    };

    function syncTheme() {
        var isLight = false;
        try {
            var u = (window.location && window.location.href) ? window.location.href : '';
            if (u.indexOf('theme=light') !== -1 || u.indexOf('mode=light') !== -1) {
                isLight = true;
            } else if (u.indexOf('theme=cyber') !== -1 || u.indexOf('mode=cyber') !== -1) {
                isLight = false;
            } else {
                isLight = (localStorage.getItem(THEME_KEY) === 'light');
            }
        } catch(e) {
            isLight = docEl.getAttribute('data-theme') === 'light';
        }
        setVisualTheme(isLight);
    }

    // Run immediately
    syncTheme();

    // Hook listeners
    function setupListeners() {
        syncTheme();

        var btn = document.getElementById('theme-switch-btn');
        if (btn && !btn._bound) {
            btn._bound = true;
            btn.addEventListener('click', window.toggleMinotmTheme);
        }

        var resumeBtn = document.getElementById('btn-quick-resume');
        if (resumeBtn && !resumeBtn._bound) {
            resumeBtn._bound = true;
            resumeBtn.addEventListener('click', window.resumeAllFlows);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupListeners);
    } else {
        setupListeners();
    }

    window.addEventListener('keydown', function(e) {
        if (e.altKey && (e.key === 't' || e.key === 'T')) {
            e.preventDefault();
            window.toggleMinotmTheme();
        }
    });
})();
