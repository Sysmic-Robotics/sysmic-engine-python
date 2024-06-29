#ifndef FIELD_H
#define FIELD_H 

#include <SFML/Graphics.hpp>
#include "config.hpp"

class Field{
    private:
        sf::CircleShape midfield_circle;

    public:
        Field(){
            float circle_radius = (config::MIDFIELD_CIRCLE_RADIUS/config::ROBOCUP_LONG)*config::window_wide;
            midfield_circle  = sf::CircleShape( (circle_radius) );
            midfield_circle.setOutlineThickness(1); 
            midfield_circle.setFillColor(sf::Color(0, 0, 0, 0));
            midfield_circle.setPosition( config::window_wide/2 - circle_radius ,  config::window_long/2 - circle_radius );
        }

        void render(sf::RenderWindow* window){
             sf::Vertex center_line[] =
            {
                sf::Vertex(sf::Vector2f(config::window_wide/2, 0)),
                sf::Vertex(sf::Vector2f(config::window_wide/2, config::window_long)),
            };
             sf::Vertex center_line2[] =
            {
                sf::Vertex(sf::Vector2f(0, config::window_long/2)),
                sf::Vertex(sf::Vector2f(config::window_wide, config::window_long/2)),
            };
            window->draw(center_line, 2, sf::Lines );
            window->draw(center_line2 ,2, sf::Lines);

            window->draw(midfield_circle); 

        }

};

#endif