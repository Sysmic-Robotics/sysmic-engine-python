const {app, BrowserWindow} = require('electron')

function createWindow () {
	// Create the browser window
	const win = new BrowserWindow({
		width: 800,
		height: 600,
		webPreferences: {
			nodeIntegration: true
		}
	});

	win.loadFile('index.html');
	win.setMenu(null);
	win.maximize();

	// Open the DevTools
	win.webContents.openDevTools()
}

app.whenReady().then(createWindow);

// macOs specific code
app.on('window-all-closed', () => {
	if (process.platform !== 'darwin') {
		app.quit();
	}
});

app.on('activate', () => {
	if (BrowserWindow.getAllWindows().length === 0) {
		createWindow();
	}
});
