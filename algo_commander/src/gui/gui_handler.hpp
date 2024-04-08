#ifndef GUI_HANDLER_H
#define GUI_HANDLER_H
#include <iostream>
#include <SFML/Graphics.hpp>
#include <imgui.h>
#include "../packet_sender.hpp"

enum CreateRouteState{
    NOTHING,
    POINT_A,
    POINT_B,
};


class GuiHandler{
    private:
        sf::CircleShape point_a;
        sf::CircleShape point_b;
        sf::CircleShape* current_point;
        bool left_mouse_clicked = false;
        bool is_pointing = false; 
        CreateRouteState active_state = NOTHING;
        PacketSender packet_sender;

    public:
        GuiHandler(){
            point_a = sf::CircleShape(10);
            point_b = sf::CircleShape(10);
            point_a.setOrigin(10,10);
            point_b.setOrigin(10,10);
            point_a.setFillColor( sf::Color::Blue );
            point_b.setFillColor( sf::Color::Red );
        }

        void input(sf::Event* event, sf::RenderWindow& window){
            // Check for mouse button pressed event
            left_mouse_clicked = false;
            if (event->type == sf::Event::MouseButtonPressed){
                if (event->mouseButton.button == sf::Mouse::Left){
                    left_mouse_clicked = true;
                    sf::Vector2i mousePosition = sf::Mouse::getPosition(window);
                }
            }
        }

        void process(sf::RenderWindow& window){
            float x = sf::Mouse::getPosition(window).x;
            float y = sf::Mouse::getPosition(window).y;

            
            switch (active_state){
                case NOTHING:
                    /* code */
                    break;
                case POINT_A:
                    point_a.setPosition(x,y); 
                    if(left_mouse_clicked){
                        active_state = POINT_B;
                        left_mouse_clicked = false;
                    }
                    break;
                case POINT_B:
                    point_b.setPosition(x,y);
                    if(left_mouse_clicked){
                        active_state = NOTHING;
                    }
                    break;
                }
        }

        void render(sf::RenderWindow* window){
            ImGui::SetNextWindowSize( ImVec2(300 , window->getSize().y ) );
            ImGui::SetNextWindowPos( ImVec2(config::window_wide, 0 ) );
            ImGui::Begin("Menu", nullptr,  ImGuiWindowFlags_NoCollapse || ImGuiWindowFlags_NoMove);
            if(ImGui::Button("Create route")){
                active_state = POINT_A;
            };

            if(ImGui::Button("Create")){
                packet_sender.request_path( point_a.getPosition(), point_b.getPosition());
            };

            if(ImGui::Button("Clear")){

            };
            ImGui::End();

            switch (active_state){
                case NOTHING:
                    window->draw(point_a);
                    window->draw(point_b);
                    break;
                case POINT_A:
                    window->draw(point_a);
                    break;
                case POINT_B:
                    window->draw(point_a);
                    window->draw(point_b);
            }
        }
};



#endif