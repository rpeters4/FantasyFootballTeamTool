#include "main.cpp"

using std::string;
using std::vector;

class Player
{
private:
    unsigned short int pos;             //player position ID number
    vector<float> ppg;                  //points scored by player in game
    unsigned int PID;			//player ID number for database
    bool injured;			//boolean flag indicates that player is injured
    /*
        various pointers, intialize to NULL will go here.
        they will be used for specific stats that should
        be tracked for any player in general.  the irrelevant
        stats for different positions will remain NULL, while
        the relevant stats will be assigned values on the fly
    */

public:
    Player();                           //ctor
    Player(const Player& cpyply);       //cctor
    ~Player();                            //dtor
    void update();                      //public update fnc
    vector<float> getStats();           //public get fnc
    
};
