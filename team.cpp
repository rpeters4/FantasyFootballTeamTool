using std::string;
using std::cout;
using std::cin;

Team::Team()
{
}

Team::Team(const Team& cpyteam)
{
}
Team::~Team()
{
}
void Team::update()
{
    //iteratively run each player's update function
}
void addPlayer()
{
    //promt user to add player to team
}
void addPlayer(string playerName)
{
    //add player based on PlayerName using API
}

void removePlayer()
{
    //prompt user to remove player from lineup
}

void removePlayer(string playerName)
{
    //remove player based on PlayerName
}

void removePlayer(unsigned int playerID)
{
    //remove player based on playerID#
}

void trade()
{
    //promt user to input players to trade as well as team to trade to/from
}

void trade(string TeamToTrade, vector<string> toPlayers, vector<string> fromPlayers)
{
    //trade player from TeamToTrade to *this from vector lists of toPlayers
    //and fromPlayers
}
