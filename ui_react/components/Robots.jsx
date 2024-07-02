import React from "react";

function Robots(){

    function draw() {
		let container = shadowRoot.getElementById("robots");
		for (let robot of Data.blue_robots) {
			let elem = shadowRoot.getElementById(`robot-${robot.id}`);
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
						<div className="flex flex-col items-center m-4 pb-3 bg-white rounded-lg border shadow-md md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">
							<img className="p-3 h-auto w-20 rounded-t-lg md:rounded-none md:rounded-l-lg" src="components/robots-panel/imgs/b${robot.id}.png" width=10></img>
							<div className="flex flex-col justify-between p-4 leading-normal">
								<p className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Robot ${robot.id}</p>
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

		/*
		for (let robot of Data.blue_robots) {
			let elem = shadowRoot.getElementById(`robot-${robot.id}`);
			if (robot.selected) {
				elem.classList.add("selected");
			}
			else {
				elem.classList.remove("selected");
			}
		}		
		*/

	}

    return(
        <div id="robots" className="flex-1 overflow-y-auto overflow-x-hidden h-full">
			<div className="flex flex-col items-center m-4 pb-3 bg-robots rounded-lg border shadow-md hover:bg-robots-hover cursor-pointer">
				<img className="p-3 h-auto w-20 rounded-t-lg md:rounded-none md:rounded-l-lg" src="../assets/robots/b0.png"></img>
				<div className="flex flex-col justify-between p-4 leading-normal">
					<p className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Robot 0</p>
				</div>
			</div>

			<div className="flex flex-col items-center m-4 pb-3 bg-robots rounded-lg border shadow-md hover:bg-robots-hover cursor-pointer">
				<img className="p-3 h-auto w-20 rounded-t-lg md:rounded-none md:rounded-l-lg" src="../assets/robots/b1.png"></img>
				<div className="flex flex-col justify-between p-4 leading-normal">
					<p className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Robot 1</p>
				</div>
			</div>
			<div className="flex flex-col items-center m-4 pb-3 bg-robots rounded-lg border shadow-md hover:bg-robots-hover cursor-pointer">
				<img className="p-3 h-auto w-20 rounded-t-lg md:rounded-none md:rounded-l-lg" src="../assets/robots/b2.png"></img>
				<div className="flex flex-col justify-between p-4 leading-normal">
					<p className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Robot 2</p>
				</div>
			</div>
			<div className="flex flex-col items-center m-4 pb-3 bg-robots rounded-lg border shadow-md hover:bg-robots-hover cursor-pointer">
				<img className="p-3 h-auto w-20 rounded-t-lg md:rounded-none md:rounded-l-lg" src="../assets/robots/b3.png"></img>
				<div className="flex flex-col justify-between p-4 leading-normal">
					<p className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Robot 3</p>
				</div>
			</div>
			<div className="flex flex-col items-center m-4 pb-3 bg-robots rounded-lg border shadow-md hover:bg-robots-hover cursor-pointer">
				<img className="p-3 h-auto w-20 rounded-t-lg md:rounded-none md:rounded-l-lg" src="../assets/robots/b4.png"></img>
				<div className="flex flex-col justify-between p-4 leading-normal">
					<p className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Robot 4</p>
				</div>
			</div>
        </div>
    )
}

export default Robots