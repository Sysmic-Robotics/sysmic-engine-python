const dgram = require('dgram');
const server = dgram.createSocket('udp4');
const Messages = require("./protobuf/ui_messages_pb");

server.on('listening', () => {
	const address = server.address();
	console.log(`server listening ${address.address}:${address.port}`);
});

server.on('message', (msg, rinfo) => {
	let package = Messages.EnginePackage.deserializeBinary(msg);
	let scene = package.getScene();

	// Get FPS
	Data.fps = package.getFps();

	// Get AIEnvironment
	if (package.getAiEnvironment().getName() == "default") {
		let environment = package.getAiEnvironment();
		Data.aiEnvironment = {
			name: environment.getName(),
			robotDestinations: []
		}

		let destinations = environment.getRobotDestinationsList();
		for (let destination of destinations) {
			Data.aiEnvironment.robotDestinations.push({
				id: destination.getId(),
				x: destination.getX() / 10 + 480, // Transform to canvas coordinate system
				y: -destination.getY() / 10 + 330  // Transform to canvas coordinate system
			})
		}
	}

	// Update ball
	Data.ball = {
		x: scene.getBall().getX() / 10 + 480,  // Transform to canvas coordinate system
		y: -scene.getBall().getY() / 10 + 330, // Transform to canvas coordinate system
		z: scene.getBall().getZ() / 10
	}

	// Update blue robots
	let copy = [];
	let blue_robots = scene.getBlueRobotsList();
	while (blue_robots.length > 0) {
		let robot = blue_robots.pop();
		let stored = Data.blue_robots.find(function(x) {return x.id === robot.getId()});
		if (stored === undefined) {
			copy.push({
				id: robot.getId(),
				x:  robot.getX() / 10 + 480,  // Transform to canvas coordinate system
				y: -robot.getY() / 10 + 330,  // Transform to canvas coordinate system
				orientation: -robot.getOrientation(), // Transform to canvas coordinate system
				velX: robot.getVelX(),
				velY: -robot.getVelY(),
				selected: false,
				radius: 9
			});
		}
		else {
			stored.x =  robot.getX() / 10 + 480;  // Transform to canvas coordinate system
			stored.y = -robot.getY() / 10 + 330;  // Transform to canvas coordinate system
			stored.orientation = -robot.getOrientation(); // Transform to canvas coordinate system
			stored.velX = robot.getVelX();
			stored.velY = -robot.getVelY();
			copy.push(stored);
		}
	}
	Data.blue_robots = copy;

	// Update yellow robots
	Data.yellow_robots.length = 0;
	let yellow_robots = scene.getYellowRobotsList();
	for (let robot of yellow_robots) {
		Data.yellow_robots.push({
			id: robot.getId(),
			x:  robot.getX() / 10 + 480, // Transform to canvas coordinate system
			y: -robot.getY() / 10 + 330, // Transform to canvas coordinate system
			orientation: -robot.getOrientation(), // Transform to canvas coordinate system
			radius: 9
		});
	}

	// Tell components to update
	let e = new CustomEvent('update');
	document.dispatchEvent(e);
});

server.on('error', (err) => {
	console.log(`server error:\n${err.stack}`);
	server.close();
});


server.bind(33333, '127.0.0.1');

// Send messages from UI to engine
setInterval(function() {
	while (Data.toBeSended.length != 0) {
		const message = Data.toBeSended.pop();
		server.send(message, 10021);
	}
}, 1000/60);
