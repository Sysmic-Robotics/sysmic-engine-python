(function() {
// Get current dir
let scripts = document.getElementsByTagName("script");
let path = scripts[scripts.length-1].src.substr(7);
let componentsDir = mydir= path.split('/').slice(0, -1).join('/');

// Component definition
class RobotsPanel extends HTMLElement {
	constructor() {
		super();

		// Component initialization
		this.attachShadow({mode: "open"});

		const t = document.createElement("template");
		t.innerHTML = `
			<link rel="stylesheet" href="node_modules/@fortawesome/fontawesome-free/css/all.min.css">
			<link href="src/style.css" rel="stylesheet" type="text/css">
			<div id="robots" class="p-3 m-3">
				
			</div>
		`;
		this.shadowRoot.appendChild(t.content.cloneNode(true));

		let self = this;
		document.addEventListener("update", function(e) {
			self.draw();
		});
	}

	draw() {
		let container = this.shadowRoot.getElementById("robots");
		for (let robot of Data.blue_robots) {
			let elem = this.shadowRoot.getElementById(`robot-${robot.id}`);
			if (elem == undefined || container.children.length != Data.blue_robots.length) {
				Data.blue_robots = Data.blue_robots.sort(function(a, b) {
					if (a.id < b.id) return -1;
					if (a.id > b.id) return  1;
					else             return  0;
				});

				container.innerHTML = "";
				for (let robot of Data.blue_robots) {
					let robotItem = document.createElement("div");
					robotItem.classList.add("robot");
					robotItem.id = `robot-${robot.id}`;
					robotItem.innerHTML = `
						<div class="flex flex-col items-center m-4 pb-3 bg-white rounded-lg border shadow-md md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">
							<img class="p-3 h-auto w-20 rounded-t-lg md:rounded-none md:rounded-l-lg" src="components/robots-panel/imgs/b${robot.id}.png" width=10></img>
							<div class="flex flex-col justify-between p-4 leading-normal">
								<p class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Robot ${robot.id}</p>
							</div>
						</div>
					`;
					container.appendChild(robotItem);

					let self = this;
					robotItem.addEventListener("click", function(e) {
						for (let robot of Data.blue_robots) {
							robot.selected = false;
						}

						robot.selected = true;

						e.stopPropagation();
					});
				}
				break;
			}
		}

		for (let robot of Data.blue_robots) {
			let elem = this.shadowRoot.getElementById(`robot-${robot.id}`);
			if (robot.selected) {
				elem.classList.add("selected");
			}
			else {
				elem.classList.remove("selected");
			}
		}
	}
}
window.customElements.define("robots-panel", RobotsPanel);
})();
