chrome.runtime.onInstalled.addListener(() => {
    console.log('AccessAI Navigator installed');
    chrome.storage.local.set({
        selectedProfile: 'visual',
        readingLevel: 'middle-school',
        targetLanguage: 'auto',
        offlineMode: true
    });
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'processAI') {
        processWithAI(request.data).then(result => {
            sendResponse({success: true, result: result});
        });
        return true;
    }
});

async function processWithAI(data) {
    return {
        processed: true,
        message: 'AI processing complete (demo mode)'
    };
}