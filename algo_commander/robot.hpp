#ifndef ROBOT_H
#define ROBOT_H

#include <iostream>
#include <SFML/Graphics.hpp>
#include <math.h> 
#include "config.hpp"

const sf::Color BLUE_TEAM_COLOR(6, 61, 155); 
const sf::Color YELLOW_TEAM_COLOR(206, 212, 41); 

class Robot {
private:
    double x; 
    double y; 
    double r;
    double angle; // IN RADS
    sf::CircleShape shape;
    
public:
    // Constructor to initialize the robot's position
    Robot(float pos_x, float pos_y, bool blue_team){
        x = pos_x;
        y = pos_y;
        angle = 0.0;
        r = (config::ROBOT_SHAPE_RADIUS/config::ROBOCUP_LONG)*config::window_wide;
        shape = sf::CircleShape(r);
        if(blue_team){
            shape.setFillColor( BLUE_TEAM_COLOR );
        }else{
            shape.setFillColor( YELLOW_TEAM_COLOR );
        }
        shape.setPosition(x - r, y - r);
    };

    void process(float delta){
        /*
        double next_x = delta*20;
        double next_y = delta*0;
        setPosition(x + next_x, y + next_y);
        */
    }

    void render(sf::RenderWindow* window){
        // Rotate vector (1,0)
        double dir_x = 1 * cos(angle)*r;
        double dir_y = 1 * sin(angle)*r;
        dir_x += x;
        dir_y += y;
        sf::Vertex dir_line[] = {
        sf::Vertex( sf::Vector2f(dir_x, dir_y) ),
        sf::Vertex( sf::Vector2f(x, y) ) };
        window->draw(shape);
        window->draw(dir_line, 2, sf::Lines);
    }

    // Method to move the robot to a new position
    void setPosition(double new_x, double new_y, float new_angle) {
        x = new_x;
        y = new_y;
        angle = new_angle;
        shape.setPosition(new_x - r, new_y - r);
        
    }


    // Method to display the current position of the robot
    void displayPosition() const {
        std::cout << "Robot Position: (" << x << ", " << y << ")\n";
    }
};

#endif