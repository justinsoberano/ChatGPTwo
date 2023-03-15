'use strict';

module.exports = function isCancel(value) {
  return !!(value && value.__CANCEL__);
};

// Path: src/axios/lib/cancel/Cancel.js
