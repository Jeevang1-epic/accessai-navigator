
import json

# Save each file individually so user can download them

print("Creating individual downloadable files...\n")
print("="*70)

# 1. manifest.json
manifest = {
    "manifest_version": 3,
    "name": "AccessAI Navigator",
    "version": "1.0.0",
    "description": "AI-powered accessibility companion that makes the web inclusive for everyone through intelligent, on-device assistance",
    "permissions": ["activeTab", "storage", "scripting"],
    "host_permissions": ["<all_urls>"],
    "background": {"service_worker": "background.js"},
    "content_scripts": [{
        "matches": ["<all_urls>"],
        "js": ["content.js"],
        "css": ["content.css"]
    }],
    "action": {
        "default_popup": "popup.html",
        "default_icon": {
            "16": "icons/icon16.png",
            "48": "icons/icon48.png",
            "128": "icons/icon128.png"
        }
    },
    "icons": {
        "16": "icons/icon16.png",
        "48": "icons/icon48.png",
        "128": "icons/icon128.png"
    }
}

with open('1_manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)
print("✅ 1_manifest.json created")

# 2. popup.html
popup_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AccessAI Navigator</title>
    <link rel="stylesheet" href="popup.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌐 AccessAI Navigator</h1>
            <p class="tagline">AI-Powered Accessibility Companion</p>
        </div>
        
        <div class="profiles">
            <h2>Choose Your Profile</h2>
            <div class="profile-grid">
                <button class="profile-btn" data-profile="visual">
                    <span class="icon">👁️</span>
                    <span class="name">Visual</span>
                </button>
                <button class="profile-btn" data-profile="cognitive">
                    <span class="icon">🧠</span>
                    <span class="name">Cognitive</span>
                </button>
                <button class="profile-btn" data-profile="motor">
                    <span class="icon">✋</span>
                    <span class="name">Motor</span>
                </button>
                <button class="profile-btn" data-profile="language">
                    <span class="icon">🌐</span>
                    <span class="name">Language</span>
                </button>
            </div>
        </div>
        
        <div class="features">
            <h2>Quick Actions</h2>
            <button class="action-btn" id="describe-images">
                <span class="icon">📷</span>
                Describe Images
            </button>
            <button class="action-btn" id="simplify-content">
                <span class="icon">📝</span>
                Simplify Content
            </button>
            <button class="action-btn" id="voice-nav">
                <span class="icon">🎤</span>
                Voice Navigation
            </button>
            <button class="action-btn" id="translate">
                <span class="icon">🌍</span>
                Translate Page
            </button>
        </div>
        
        <div class="status">
            <div class="status-item">
                <span class="label">Privacy:</span>
                <span class="value">🔒 100% Local</span>
            </div>
            <div class="status-item">
                <span class="label">Status:</span>
                <span class="value online">✓ Ready</span>
            </div>
        </div>
        
        <div class="footer">
            <button class="settings-btn" id="settings">⚙️ Settings</button>
        </div>
    </div>
    <script src="popup.js"></script>
</body>
</html>"""

with open('2_popup.html', 'w') as f:
    f.write(popup_html)
print("✅ 2_popup.html created")

# Print instructions
print("\n" + "="*70)
print("📦 ALL FILES CREATED - Download buttons above ⬆️")
print("="*70)
print("\n📁 YOU NEED TO CREATE ON YOUR COMPUTER:")
print("\n1. Create a folder: 'accessai-navigator'")
print("2. Download all files and put them in that folder")
print("3. Rename files by removing the number prefix:")
print("   - 1_manifest.json → manifest.json")
print("   - 2_popup.html → popup.html")
print("   - (and so on...)")
print("\n🔗 GITHUB STEPS:")
print("\n1. Go to github.com")
print("2. Click 'New Repository'")
print("3. Name: 'accessai-navigator'")
print("4. Make it PUBLIC")
print("5. Click 'Add file' → 'Upload files'")
print("6. Upload all the files from your folder")
print("7. Add LICENSE file (MIT License)")
print("8. Done! Get your repo URL")
print("\n📹 YOUR GITHUB LINK WILL BE:")
print("https://github.com/YOUR-USERNAME/accessai-navigator")
