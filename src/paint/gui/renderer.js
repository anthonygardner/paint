// get html files
const dirPath = path.join(process.cwd(), "..", "..", "..", "results", "html");
const htmlFiles = fs.readdirSync(dirPath, (err, files) => files.filter((e) => path.extname(e).toLowerCase() === ".html"));

// create tabs
const tabGroup = document.querySelector("tab-group");

for (var tabNumber = 0; tabNumber < htmlFiles.length; tabNumber++) {
    tabGroup.addTab({
        title: htmlFiles[tabNumber],
        src: path.join(dirPath, htmlFiles[tabNumber]),
        active: true,
        visible: true
    });
};
