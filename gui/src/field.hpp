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

        // Transform robocup coordinates to global window coordinates
        /*
        sf::Vector2f transform_to_window(sf::Vector2f original_vec){
            // transform to window coordinates

            // transform to 
            return sf::Vector2f(original_vec.x )
        }*/

        void render(sf::RenderWindow* window){
            // Field Limits
            sf::RectangleShape field_limit(sf::Vector2f(FIELD_DIMENSIONS::X_MAX, FIELD_DIMENSIONS::Y_MAX));
            field_limit.setPosition(FIELD_DIMENSIONS::OFFSET_X, FIELD_DIMENSIONS::OFFSET_Y);
            field_limit.setFillColor(sf::Color::Transparent);
            field_limit.setOutlineColor(sf::Color::White);
            field_limit.setOutlineThickness(5.0f);
            window->draw(field_limit);
            // inside limit
            sf::RectangleShape field_limit2(sf::Vector2f(FIELD_DIMENSIONS::X_MAX, FIELD_DIMENSIONS::Y_MAX));
            field_limit.setPosition(FIELD_DIMENSIONS::OFFSET_X, FIELD_DIMENSIONS::OFFSET_Y);
            field_limit.setFillColor(sf::Color::Transparent);
            field_limit.setOutlineColor(sf::Color::White);
            field_limit.setOutlineThickness(5.0f);
            window->draw(field_limit);

            window->draw(midfield_circle); 

        }

};

#endif