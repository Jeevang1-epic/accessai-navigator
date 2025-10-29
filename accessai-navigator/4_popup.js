document.addEventListener('DOMContentLoaded', function() {
    const profileBtns = document.querySelectorAll('.profile-btn');
    profileBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const profile = this.dataset.profile;
            chrome.storage.local.set({ selectedProfile: profile });
            this.style.background = '#e0e7ff';
            setTimeout(() => {
                this.style.background = 'white';
            }, 200);
        });
    });

    document.getElementById('describe-images').addEventListener('click', function() {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {action: 'describeImages'});
        });
    });

    document.getElementById('simplify-content').addEventListener('click', function() {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {action: 'simplifyContent'});
        });
    });

    document.getElementById('voice-nav').addEventListener('click', function() {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {action: 'voiceNav'});
        });
    });

    document.getElementById('translate').addEventListener('click', function() {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {action: 'translate'});
        });
    });
});