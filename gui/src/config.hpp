#ifndef CONFIG_H
#define CONFIG_H

// Este archivo principalmente es para calcular transformar la geometria de la cancha a la pantalla

namespace config{
    // These are the real dimensions (of the real word :O)
    // Robocup dimensions B League in meters 
    const float ROBOCUP_LONG = 9; // Robocup field long
    const float ROBOCUP_WIDE = 6; // Robocup field wide
    const float MIDFIELD_CIRCLE_RADIUS = 0.5;
    const float ROBOT_SHAPE_RADIUS = 0.09; // 0.18m/2

    // window measures
    int window_wide = 800; // our robocup virtual field long
    int window_long = window_wide/(ROBOCUP_LONG/ROBOCUP_WIDE);
}

namespace ROBOCUP_DIMENSIONS{
    // ROBOCUP LEAGUE B FIELD DIMENSIONS
    // Source: https://robocup-ssl.github.io/ssl-rules/sslrules.html#:~:text=2.1.,-1.&text=The%20field%20of%20play%20must,9%20meters%20times%206%20meters
    const float WIDE = 10.400;
    const float LONG = 7.400;
    const float CIRCLE_DIAMETER = 1;
    const float DEFENSE_AREA_WIDE = 1;
    const float DEFENSE_AREA_LONG = 1;
    const float GOAL_AREA_LONG = 1;
    const float PLAY_WIDE = 9;
    const float PLAY_LONG = 6;
}

namespace WINDOW_DIMENSIONS{
    // window measures
    const int WIDE = 1200; // our robocup virtual field long
    const int LONG = WIDE/(ROBOCUP_DIMENSIONS::LONG/ROBOCUP_DIMENSIONS::WIDE);
}

// Virtual field dimensions, used to draw
namespace FIELD_DIMENSIONS{
    const float WINDOW_PROPORTION = 0.8; // Number between 0 and 1
    const float OFFSET_X = ((1 - WINDOW_PROPORTION)*0.5)*config::window_wide; // where the field start on the window
    const float OFFSET_Y = 0;
    const float X_MAX = config::window_wide*WINDOW_PROPORTION;
    const float Y_MAX = config::window_long*WINDOW_PROPORTION;


}


#endif