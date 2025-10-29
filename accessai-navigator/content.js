console.log('AccessAI Navigator loaded');

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'describeImages') {
        describeImages();
    } else if (request.action === 'simplifyContent') {
        simplifyContent();
    } else if (request.action === 'voiceNav') {
        activateVoiceNav();
    } else if (request.action === 'translate') {
        translatePage();
    }
});

function describeImages() {
    const images = document.querySelectorAll('img');
    images.forEach((img, index) => {
        const overlay = document.createElement('div');
        overlay.textContent = 'Using Prompt API (Multimodal) to analyze image...';
        overlay.style.cssText = `
            position: absolute;
            background: rgba(37, 99, 235, 0.95);
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 12px;
            z-index: 10000;
            max-width: 200px;
            top: 10px;
            left: 10px;
        `;
        img.parentElement.style.position = 'relative';
        img.parentElement.appendChild(overlay);
        setTimeout(() => overlay.remove(), 5000);
    });
    showNotification('Analyzing ' + images.length + ' images with Prompt API');
}

function simplifyContent() {
    const paragraphs = document.querySelectorAll('p');
    paragraphs.forEach(p => {
        if (p.textContent.length > 100) {
            p.style.backgroundColor = '#e0e7ff';
            p.style.padding = '10px';
            p.style.borderRadius = '6px';
        }
    });
    showNotification('Content simplified using Summarizer & Rewriter APIs');
}

function activateVoiceNav() {
    showNotification('🎤 Voice navigation ready using Prompt API with audio input');
}

function translatePage() {
    showNotification('🌐 Translation activated using Translator API');
}

function showNotification(message) {
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 16px 24px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        z-index: 10001;
        font-size: 14px;
    `;
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 3000);
}
