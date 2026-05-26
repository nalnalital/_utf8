// File: export_usa_json.js - Exporte emojiKeywords de utf8_search_usa.js en JSON
// Desc: Pour que build_fr.py puisse lire la structure sans parser le JS.
// Version 1.0.0 | Copyright 2025 DNAvatar.org - Arnaud Maignan
const fs = require('fs');
const path = require('path');
const root = path.join(__dirname, '..');
const mod = require(path.join(root, 'utf8_search_usa.js'));
fs.writeFileSync(path.join(__dirname, 'emoji_usa.json'), JSON.stringify(mod.emojiKeywords, null, 0), 'utf8');
console.log('wip/emoji_usa.json écrit.');
