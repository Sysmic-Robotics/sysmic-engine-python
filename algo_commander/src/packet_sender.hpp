#ifndef PACKET_SENDER_H
#define PACKET_SENDER_H
#include <SFML/Network.hpp>
#include <SFML/System/Vector2.hpp>
#include <iostream>

#include "algo_commander.pb.h"

class PacketSender {
    public:
        PacketSender()  {
            if (m_socket.bind(sf::Socket::AnyPort) != sf::Socket::Done) {
                std::cerr << "Failed to bind to port" << std::endl;
            }
            m_socket.setBlocking(false);
        }

        // Request pathfinder between two points
        void request_path(sf::Vector2f from_point, sf::Vector2f to_point){
            // Convert to global coords
            from_point = convert_to_global_coords(from_point.x, from_point.y);
            to_point = convert_to_global_coords(to_point.x, to_point.y);

            algo_commander::RequestPath request_path;
            
            algo_commander::Vector2f* point1 = request_path.mutable_from_point();
            point1->set_x(from_point.x);
            point1->set_y(from_point.y);

            algo_commander::Vector2f* point2 = request_path.mutable_to_point();
            point2->set_x(to_point.x);
            point2->set_y(to_point.y);

            // Serialize the RequestPath message into a string
            std::string serialized_data;
            request_path.SerializeToString(&serialized_data);
            std::cout << "Point 1: " << from_point.x << " , " << from_point.y << "\n";
            std::cout << "Point 2: " << to_point.x << " , " << to_point.y  << "\n";
            std::cout << "Serialized data: " << serialized_data.size() << "\n";
            send_packet(serialized_data);
        }

    private:
        sf::UdpSocket m_socket;
        unsigned short m_port = 5656;
        sf::Vector2f convert_to_global_coords(float local_x, float local_y){
            local_x -= config::window_wide/2;
            local_y -= config::window_long/2;

            // Aumentar el espacio
            float global_x =  ((config::ROBOCUP_LONG)*1000*local_x)/(config::window_wide);
            float global_y = ((config::ROBOCUP_LONG)*1000*local_y)/(config::window_wide);
            global_y = global_y*-1; // reflection


            sf::Vector2f global_coords; 
            global_coords.x = global_x;
            global_coords.y = global_y;
            return global_coords;
        }

        bool send_packet(std::string packet) {
            sf::Socket::Status result = m_socket.send(packet.c_str(), packet.size(), sf::IpAddress::getLocalAddress(), 5656);

            if (result != sf::Socket::Done) {
                std::cerr << "Failed to send packet" << std::endl;
                return false;
            }

            return true;
        }
};

#endif