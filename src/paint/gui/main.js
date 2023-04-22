// import packages
const { app, BrowserWindow, Menu } = requre("electron");
const path = require("path");

// configure environment variables
// const isDev = process.env.NODE_ENV !== "production";
const isMac = process.platform === "darwin";

// create main window
function createWindow () {
    const window = new BrowserWindow({
        title: "paint",
        width: 800,
        height: 600,
        webPreferences: {
            contextIsolation: true,
            nodeIntegration: true,
            preload: path.join(__dirname, "preload.js"),
            webviewTag: true
        }
    });

    // open devtools if dev environment is activated
    // if (isDev) {
        // window.webContents.openDevTools();
    // }

    window.loadFile(path.join(__dirname, "index.html"));
};

// build app
app.whenReady().then(() => {
    createWindow();
    
    const mainMenu = Menu.buildFromTemplate(menu);
    Menu.setApplicationMenu(mainMenu);

    app.on("activate", () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

const menu = [
    {
        label: "File",
        submenu: [
            {
                label: "Quit",
                click: () => app.quit(),
                accelerator: "Ctrl+Q"
            }
        ]
    }
]

app.on("window-all-closed", () => {
    if (!isMac) {
        app.quit();
    }
});
