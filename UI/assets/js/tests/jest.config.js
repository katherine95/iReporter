const setupTestFrameworkScriptFile = 'ireporter.test.js';
export { setupTestFrameworkScriptFile as default };
const { defaults } = require('jest-config');

module.exports = {
  // ...
  moduleFileExtensions: [...defaults.moduleFileExtensions, 'ts', 'tsx'],
  // ...
};