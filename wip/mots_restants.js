// File: mots_restants.js - Liste des mots encore en anglais (sans doublons) -> restant_{lang}.json
// Desc: Usage: node mots_restants.js fr
// Version 1.0.0 | Copyright 2025 DNAvatar.org - Arnaud Maignan
const fs = require('fs');
const path = require('path');
const lang = process.argv[2] || 'fr';
const root = path.join(__dirname, '..');
const usa = require(path.join(root, 'utf8_search_usa.js')).emojiKeywords;
const current = require(path.join(root, 'utf8_search_' + lang + '.js')).emojiKeywords;
const restants = {};
for (const emoji of Object.keys(usa)) {
  const enKws = usa[emoji] || [];
  const curKws = current[emoji] || [];
  for (let i = 0; i < enKws.length; i++) {
    if (curKws[i] === enKws[i]) restants[enKws[i]] = '';
  }
}
const out = path.join(__dirname, 'restant_' + lang + '.json');
fs.writeFileSync(out, JSON.stringify(restants, null, 2), 'utf8');
console.log('wip/restant_' + lang + '.json écrit: ' + Object.keys(restants).length + ' mots à traduire.');
