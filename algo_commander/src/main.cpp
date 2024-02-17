#include <SFML/Graphics.hpp>
#include <iostream>
#include <thread>

#include "imgui.h"
#include "imgui-SFML.h"

#include "packet_receiver.hpp"
#include "packet_handler.hpp"
#include "field.hpp"
#include "robot_handler.hpp"
#include "route_handler.hpp"


// Main loop
int main(){
    sf::RenderWindow window =  sf::RenderWindow (sf::VideoMode(config::window_wide, config::window_long), "Robocup SSL");
    ImGui::SFML::Init(window);
    PacketReceiver packet_listener(12345);
    
    
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
    
    sf::Clock clock;
    while(window.isOpen()){
        // Inputs
        sf::Event event;
        while (window.pollEvent(event)){
            ImGui::SFML::ProcessEvent(event);
            if (event.type == sf::Event::Closed)
                window.close();
        }
        // Process
        ImGui::SFML::Update(window, clock.restart() );
        float delta_time = clock.getElapsedTime().asSeconds();
        std::vector<char> packets = packet_listener.get_packets();
        packet_handler.handle_packets(packets);
        robots.process(delta_time);

        // Render
        
        window.clear( sf::Color(128, 128, 128) );

        field.render( &window );
        robots.render(&window);
        route_handler.render(&window);
        ImGui::SFML::Render(window);
        window.display();
    }
    ImGui::SFML::Shutdown();
    
    return 0;
}


