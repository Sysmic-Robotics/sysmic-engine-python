#ifndef PACKET_RECEIVER_H
#define PACKET_RECEIVER_H
#include <SFML/Network.hpp>
#include <iostream>
#include <vector>

//#include "src/proto/algo_commander.pb.h" // Include the generated header file
constexpr int BUFFER_SIZE = 1024*2;

class PacketReceiver{
    private:
        sf::UdpSocket socket;

    public:
        PacketReceiver(int port) {
            // UDP socket for receiving packets
            if (socket.bind(port) != sf::Socket::Done) {
                std::cerr << "Failed to bind socket to port " << port << std::endl;
            }
            std::cout << "Socket bound to port " << port << std::endl;
            socket.setBlocking(false);
    }

    ~PacketReceiver() {
        
    }

    std::vector<char> get_packets() {
        sf::IpAddress sender;
        unsigned short senderPort;
        std::vector<char> buffer(BUFFER_SIZE);
        std::size_t received;
        sf::Socket::Status status = socket.receive(buffer.data(), buffer.size(), received, sender, senderPort);
        if (status != sf::Socket::Done) {
            //std::cerr << "Error receiving packet: " << status << std::endl;
            return std::vector<char>();
        }
        buffer.resize(received);
        //std::cout << "Received " << received << " bytes from " << sender << ":" << senderPort << std::endl;

        return buffer;
    }


};

#endif