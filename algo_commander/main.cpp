#include <SFML/Graphics.hpp>
#include <iostream>
#include <thread>

#include "packet_receiver.hpp"
#include "packet_handler.hpp"
#include "field.hpp"
#include "robot_handler.hpp"
#include "route_handler.hpp"

std::vector<float> convert_to_local_coords(float global_x, float global_y){

            // Comprimir el espacio
            float local_x =  (global_x*config::window_wide)/((config::ROBOCUP_LONG)*1000);
            float local_y = (global_y*config::window_long)/((config::ROBOCUP_WIDE)*1000);
            local_y = local_y*-1; // reflection
            local_x += config::window_wide/2;
            local_y += config::window_long/2;

            std::vector<float> local_coords(2); 
            local_coords[0] = local_x;
            local_coords[1] = local_y;
            return local_coords;
}

// Main loop
int main(){
    sf::RenderWindow window =  sf::RenderWindow (sf::VideoMode(config::window_wide, config::window_long), "Robocup SSL");
    PacketReceiver packet_listener(12345);
    
    sf::Clock clock;
    // Objects
    Field field;
    RobotHandler robots;
    // Create team blue
    robots.add_robot(400,200, true);
    
    robots.add_robot(400,300, true);
    robots.add_robot(400,400, true);
    robots.add_robot(400,500, true);
    robots.add_robot(400,600, true);
    robots.add_robot(400,700, true);

    // Create team yellow
    robots.add_robot(1000,200, false);
    robots.add_robot(1000,300, false);
    robots.add_robot(1000,400, false);
    robots.add_robot(1000,500, false);
    robots.add_robot(1000,600, false);
    robots.add_robot(1000,700, false);
    
    RouteHandler route_handler;
    PacketHandler packet_handler(&robots, &route_handler);
    
    while(window.isOpen()){
        float delta_time = clock.restart().asSeconds();
        // Inputs
        sf::Event event;
        while (window.pollEvent(event)){
            if (event.type == sf::Event::Closed)
                window.close();
        }
        // Process
        std::vector<char> packets = packet_listener.get_packets();
        packet_handler.handle_packets(packets);
        robots.process(delta_time);

        // Render
        window.clear( sf::Color(128, 128, 128) );

        field.render( &window );
        robots.render(&window);
        route_handler.render(&window);
        
        window.display();
    }
    
    return 0;
}


