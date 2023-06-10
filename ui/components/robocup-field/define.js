(function() {

// Modules required
const { remote } = require('electron')
const { Menu, MenuItem } = remote
const Messages = require("./protobuf/ui_messages_pb");


// Get current dir
let scripts = document.getElementsByTagName("script");
let path = scripts[scripts.length-1].src.substr(7);
let componentsDir = mydir= path.split('/').slice(0, -1).join('/');

// Component definition
class RobocupField extends HTMLElement {
	constructor() {
		super();

		// Component initialization
		this.attachShadow({mode: "open"});
		
		const t = document.createElement("template");
		t.innerHTML = `
		<script src="https://cdn.tailwindcss.com"></script>

		<div id="container" class="p-3 flex justify-center items-center">
			<div class="relative z-0">
				<object data="src/field.svg" type="image/svg+xml"></object>	
				<div class="absolute inset-0 flex justify-center items-center z-10">
					<canvas class="w-full" id="canvas" width="960" height="660" ></canvas>
				</div>		
			</div>
		</div>
		`;
		this.shadowRoot.appendChild(t.content.cloneNode(true));

		let self = this;
		document.addEventListener("update", function(e) {
			self.draw();
		});

		// Select robot
		self.addEventListener("click", function(e) {
			const rect =  self.shadowRoot.getElementById("canvas").getBoundingClientRect();
			let x = e.clientX - rect.left;
			let y = e.clientY - rect.top;
			x = (x / rect.width)  * 960; // Takes into account scaling
			y = (y / rect.height) * 660; // Takes into account scaling

			for (let robot of Data.blue_robots) {
				if (Math.sqrt((robot.x - x)**2 + (robot.y - y)**2) <= robot.radius) {
					for (let robot of Data.blue_robots) {
						robot.selected = false;
					}
					robot.selected = true;
					e.stopPropagation();
					break;
				}
			}
		});

		// Context menu
		self.addEventListener("contextmenu", function(e) {
			e.preventDefault();
			const menu = Menu.buildFromTemplate([
			{
				label: 'Move here',
				click: function() {
					// Create command
					let command = new Messages.Command();
					command.setCommandType(Messages.Command.CommandType.START_MOVE_TO);

					let ids = Data.getSelectedRobots().map(robot => robot.id);
					command.setRobotIdsList(ids);

					let destination = new Messages.Command.Position();
					const rect =  self.shadowRoot.getElementById("canvas").getBoundingClientRect();
					let x = e.clientX - rect.left;
					let y = e.clientY - rect.top;
					x = (x / rect.width)  * 960; // Takes into account scaling
					y = (y / rect.height) * 660; // Takes into account scaling
					x = (x - 480) * 10;          // Transform to grSim coordinates
					y = -(y - 330) * 10;          // Transform to grSim coordinates
					destination.setX(x);
					destination.setY(y);
					command.setDestination(destination);

					Data.toBeSended.push(command.serializeBinary());
				},
				enabled: Data.isRobotSelected()
			}
			]);
			menu.popup({window: remote.getCurrentWindow()})
		});
	}

	draw() {
		let canvas = this.shadowRoot.getElementById("canvas");
		let ctx = canvas.getContext('2d');

		// Clear
		ctx.clearRect(0, 0, canvas.width, canvas.height);

		// Draw Ai specif stuff
		if (Data.aiEnvironment.name == "default") {
			for (let destination of Data.aiEnvironment.robotDestinations) {
				ctx.beginPath();
				ctx.save();
				ctx.fillStyle = "red";
				ctx.arc(destination.x, destination.y, 2, 0, 2 * Math.PI);
				ctx.fill();
				ctx.restore();
			}
		}

		// Draw ball
		ctx.beginPath();
		ctx.fillStyle = "orange";
		ctx.arc(Data.ball.x, Data.ball.y, 2.15, 0, 2 * Math.PI, false);
		ctx.fill();

		// Draw blue robots
		for (let robot of Data.blue_robots) {
			if (robot.selected) {
				ctx.save();
				ctx.fillStyle = "rgba(62, 161, 240, 0.5)";
				ctx.beginPath();
				ctx.arc(robot.x, robot.y, robot.radius + 10, 0, 2 * Math.PI);
				ctx.fill();
				ctx.restore();
			}

			// Draw robot velocity
			ctx.beginPath();
			ctx.save();
			ctx.strokeStyle = "red";
			ctx.moveTo(robot.x, robot.y);
			ctx.lineTo(robot.x + 60 * robot.velX, robot.y + 60 * robot.velY);
			ctx.stroke();
			ctx.restore();

			// Draw orientation
			ctx.beginPath();
			ctx.save();
			ctx.strokeStyle = "white";
			ctx.lineWidth = 4;
			ctx.arc(robot.x, robot.y, robot.radius + 1, robot.orientation + 0.3, robot.orientation - 0.3, true);
			ctx.stroke();
			ctx.restore();

			// Draw robot
			ctx.beginPath();
			ctx.fillStyle = "#3399ff";
			ctx.arc(robot.x, robot.y, robot.radius, 0, 2 * Math.PI);
			ctx.fill();
			ctx.stroke();

			ctx.beginPath();
			ctx.font = "bold 16px Arial";
			ctx.fillStyle = "black";
			ctx.fillText(`${robot.id}`, robot.x - 4.5, robot.y + 6);

		}

		for (let robot of Data.yellow_robots) {
			ctx.beginPath();
			ctx.save();
			ctx.strokeStyle = "white";
			ctx.lineWidth = 4;
			ctx.arc(robot.x, robot.y, robot.radius + 1, robot.orientation + 0.3, robot.orientation - 0.3, true);
			ctx.stroke();
			ctx.restore();

			ctx.beginPath();
			ctx.fillStyle = "gold";
			ctx.arc(robot.x, robot.y, robot.radius, 0, 2 * Math.PI);
			ctx.fill();
			ctx.stroke();

			ctx.beginPath();
			ctx.font = "bold 16px Arial";
			ctx.fillStyle = "black";
			ctx.fillText(`${robot.id}`, robot.x - 4.5, robot.y + 6);
		}
	}
}
window.customElements.define("robocup-field", RobocupField);
})();
