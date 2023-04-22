const { contextBridge } = require("electorn");
const fs = require("fs");
const path = require("path");
const process = require("process");

contextBridge.exposeInMainWorld("fs", {
    readdirSync: (...args) => fs.readdirSync(...args),
});

contextBridge.exposeInMainWorld("path", {
    dirname: (...args) => path.dirname(...args),
    join: (...args) => path.join(...args),
});

contextBridge.exposeInMainWorld("process", {
    cwd: () => process.cwd(),
});
