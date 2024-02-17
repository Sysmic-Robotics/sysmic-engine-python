#ifndef PACKET_PROCESSOR_H
#define PACKET_PROCESSOR_H

#include <iostream>
#include <vector>
#include <SFML/Graphics.hpp>
#include "algo_commander.pb.h"
#include "robot_handler.hpp"
#include "route_handler.hpp"
#include "config.hpp"

class PacketHandler{
    public:
        PacketHandler(RobotHandler* robot_hd, RouteHandler* new_route_handler ){
            robot_handler = robot_hd;
            route_handler = new_route_handler;
        }

        void handle_packets(std::vector<char> packet){
            if(packet.size() > 0){
                deserialize_packet(packet);
            }
            
        }

    private:
        RobotHandler* robot_handler;
        RouteHandler* route_handler;
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
    
        void deserialize_packet(std::vector<char> serialized_data){
            algo_commander::WrapperMessage wrapper;
            if (!wrapper.ParseFromArray(serialized_data.data(), serialized_data.size())) {
                std::cerr << "Failed to parse WrapperMessage." << std::endl;
                // Esto puede pasar si se exceedio el tamaño del buffer en packet_receiver
                // Esto puede pasar si el packete esta mal serializado 
                return;
            }
            // Extract fields from the deserialized message
            int64_t commonField = wrapper.commonfield();
            
            if (wrapper.has_robot_position()) {
                const algo_commander::RobotPosition& m1 = wrapper.robot_position();
                std::vector<float> local_coords = convert_to_local_coords(m1.pos_x(), m1.pos_y() );
                robot_handler->set_robot_pos(m1.id(), local_coords[0], local_coords[1], m1.angle() ,m1.blue_team() );
            }else if (wrapper.has_route()) {
                std::cout<< "llego rut" << std::endl;
                const algo_commander::Route& m2 = wrapper.route();
                std::vector<sf::Vector2f> pointsVector;
                for (const auto& point : m2.points()) {
                    std::vector<float> vec = convert_to_local_coords(point.x(), point.y());
                    pointsVector.push_back(sf::Vector2f(vec[0], vec[1]));
                }
                route_handler->create_new_route(m2.robot_id(), m2.blue_team(), pointsVector);
            }
    
        }   
    
};

#endif