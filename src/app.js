'use strict';
const cp = require('child_process');

function evaluate(req) {
  return eval(req.query.code);
}

function shell(req) {
  cp.exec(req.query.cmd, (err, out) => {
    console.log(out);
  });
}

module.exports = { evaluate, shell };
