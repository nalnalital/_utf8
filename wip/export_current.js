// File: export_current.js - Exporte emojiKeywords du JS langue courante en JSON
// Desc: Usage: node export_current.js fr  -> wip/emoji_fr_current.json
// Version 1.0.0 | Copyright 2025 DNAvatar.org - Arnaud Maignan
const fs = require('fs');
const path = require('path');
const lang = process.argv[2] || 'fr';
const root = path.join(__dirname, '..');
const mod = require(path.join(root, 'utf8_search_' + lang + '.js'));
const out = path.join(__dirname, 'emoji_' + lang + '_current.json');
fs.writeFileSync(out, JSON.stringify(mod.emojiKeywords, null, 0), 'utf8');
console.log('wip/emoji_' + lang + '_current.json écrit.');
