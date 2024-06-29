#ifndef ROUTE_H
#define ROUTE_H

#include <SFML/Graphics.hpp>
#include <vector>

class Route{

    private:
        std::vector<sf::Vector2f> points;

    public: 
        Route(const std::vector<sf::Vector2f>& waypoints){
            points = waypoints;
        }
        
        void render(sf::RenderWindow* window) const {
            if (points.size() < 2) // A route should have at least two waypoints to draw
                return;

            sf::CircleShape circle(5);
            circle.setFillColor(sf::Color::Black); // Set color
            circle.setOrigin(5, 5); // Set origin to center

            sf::VertexArray lines(sf::LineStrip, points.size());
            for (size_t i = 0; i < points.size(); ++i) {
                lines[i].position = points[i];
                circle.setPosition(points[i]);
                window->draw(circle);
            }
            window->draw(lines);
        }
        

};


#endif