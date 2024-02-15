#ifndef CONFIG_H
#define CONFIG_H

// Este archivo principalmente es para calcular transformar la geometria de la cancha a la pantalla

namespace config{
    // Robocup dimensions B League in meters
    const float ROBOCUP_LONG = 9;
    const float ROBOCUP_WIDE = 6;
    const float MIDFIELD_CIRCLE_RADIUS = 0.5;
    const float ROBOT_SHAPE_RADIUS = 0.09; // 0.18m/2

    // window measures
    int window_wide = 1200; // our robocup virtual field long
    int window_long = window_wide/(ROBOCUP_LONG/ROBOCUP_WIDE);
}




#endif