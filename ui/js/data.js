Data = {};
Data.ball = undefined;
Data.blue_robots = [];
Data.yellow_robots = [];
Data.toBeSended = [];
Data.fps = undefined;
Data.aiEnvironment = undefined;

Data.isRobotSelected = function() {
	for (let robot of Data.blue_robots) {
		if (robot.selected) return true;
	}
	return false;
}

Data.getSelectedRobots = function() {
	let selected = [];
	for (let robot of Data.blue_robots) {
		if (robot.selected) selected.push(robot);
	}
	return selected;
}
