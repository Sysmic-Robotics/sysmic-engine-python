#ifndef ROUTE_HANDLER_H
#define ROUTE_HANDLER_H

#include <SFML/Graphics.hpp>
#include <vector>
#include <map>
#include "route.hpp"


class RouteHandler{

    private:
        std::map<std::string, Route*> robot_routes;

    public:
        void create_new_route(int robot_id, bool blue_team, std::vector<sf::Vector2f>& points){
            std::string robot_code = convert_to_robot_code(robot_id, blue_team);
            auto it = robot_routes.find(robot_code);
            if (it != robot_routes.end()) {
                delete it->second;
                robot_routes.erase(it);
            }
            robot_routes[ robot_code ] = new Route(points);
        }

        void render(sf::RenderWindow* window){
            for (const auto& pair : robot_routes) {
                const Route* route = pair.second;
                route->render(window);
            }
        } 

        std::string convert_to_robot_code(int number, bool blue_team) {
            std::string code("y");
            if(blue_team){
                code = "y";
            }
            // If the number is less than 10, prepend '0' to it
            if (number < 10) {
                return code + "0" + std::to_string(number);
            } else {
                return code + std::to_string(number);
            }
        }

};


#endif