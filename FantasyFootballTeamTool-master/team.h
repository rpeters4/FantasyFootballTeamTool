#include "player.h"

using std::vector;
using std::string;

class Team
{
private:
    vector<unsigned int> roster;

public:
    Team();
    Team(const Team& cpyteam);
    ~Team();
    void update();
    void addPlayer();
    void addPlayer(string playerName);
    void removePlayer();
    void removePlayer(string playerName);
    void removePlayer(unsigned int playerID);
    void trade();
    void trade(string TeamToTrade, vector<string> toPlayers, vector<string> fromPlayers);

};
