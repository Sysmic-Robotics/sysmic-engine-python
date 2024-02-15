#ifndef ROBOT_HANDER_H
#define ROBOT_HANDER_H


#include <SFML/Graphics.hpp>
#include <vector>
#include "robot.hpp"


class RobotHandler{
    private:
        std::vector<Robot*> robots_blue;
        std::vector<Robot*> robots_yellow;

    public:
        void add_robot(float pos_x, float pos_y, bool blue_team){
            if(blue_team){
                robots_blue.push_back(new Robot(pos_x, pos_y, blue_team));
            }else{
                robots_yellow.push_back(new Robot(pos_x, pos_y, blue_team));
            }
        }

        void render(sf::RenderWindow* window){
            for (Robot* robot : robots_blue) {
                robot->render(window);
            }
            for (Robot* robot : robots_yellow) {
                robot->render(window);
            }
        } 
        
        void set_robot_pos(int robot_id, double pos_x, double pos_y, float angle, bool blue_team){
            if(blue_team){
                if(robot_id < robots_blue.size()){
                    robots_blue[robot_id]->setPosition(pos_x, pos_y, angle);
                    return;
                }
            }else{
                if(robot_id < robots_blue.size()){
                    robots_yellow[robot_id]->setPosition(pos_x, pos_y, angle);
                    return;
                }
            }
            std::cout << " No robot id found" << std::endl;
        }
        
        void process(float delta){
            for (Robot* robot : robots_blue) {
                robot->process(delta);
            }
            for (Robot* robot : robots_yellow) {
                robot->process(delta);
            }
        }   
}; 


#endif