(function() {
// Get current dir
let scripts = document.getElementsByTagName("script");
let path = scripts[scripts.length-1].src.substr(7);
let componentsDir = mydir= path.split('/').slice(0, -1).join('/');

// Component definition
class SysmicHeader extends HTMLElement {
	constructor() {
		super();

		// Component initialization
		this.attachShadow({mode: "open"});

		const t = document.createElement("template");
		t.innerHTML = `
		<link rel="stylesheet" href="src/style.css">
		<link rel="stylesheet" href="node_modules/@fortawesome/fontawesome-free/css/all.min.css">
	
		<nav class="flex items-center bg-teal-600 p-2 flex-wrap">
			<div>
				<a href="#" class="text-white text-3xl font-bold p-3 inline-flex items-center">System Robotics</a>

				<label for="default-toggle" class="inline-flex relative items-center cursor-pointer ml-7">
					<input type="checkbox" value="" id="default-toggle" class="sr-only peer">
					<div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-red-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-red-600"></div>
				</label>
			</div>

			<div class="top-nav w-full lg:inline-flex lg:flex-grow lg:w-auto">
				<div class="lg:inline-flex lg:flex-row lg:ml-auto px-2">

					<b id="fps" class="lg:inline-flex lg:w-auto px-3 py-2 rounded text-gray-200">FPS</b>

					<select id="select" class="lg:inline-flex lg:w-auto px-4 py-2 mx-4 rounded">
						<option value="default">Default</option>
						<option value="robot-ball">Robot and Ball</option>
						<option value="robot-ball-goalkeeper">Robot, Ball and Goalkeeper</option>
					</select>
					
					<i class="fas fa-cog fa-2x" class="lg:inline-flex lg:w-auto px-5 py-2 rounded text-gray-200"></i>
				</div>
			</div>	
		</nav>

		`;
		this.shadowRoot.appendChild(t.content.cloneNode(true));

		
		// Handle events
		let self = this;
		let select = this.shadowRoot.getElementById("select");
		document.addEventListener("update", function(e) {
			self.update();
		});
		
		select.addEventListener("change", function(e) {
			let command = new Messages.Command();
			command.setCommandType(Messages.Command.CommandType.CHANGE_AI_ENVIRONMENT);
			command.setAiEnvironment(select.options[select.selectedIndex].value);
			Data.toBeSended.push(command.serializeBinary());			
		});
	}

	update() {
		this.shadowRoot.getElementById("fps").innerHTML = Data.fps + " FPS";
	}

}
window.customElements.define("sysmic-header", SysmicHeader);
})();