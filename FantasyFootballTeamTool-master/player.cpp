using std::vector<T>;
using std::string;
using std::cerr;

Player::Player()
{
    pos=0;
    //INITIALIZE PLAYER'S VALUES HERE
}

Player::Player(const Player& cpyply)
{
    this->pos = cpyply->pos;
    for (vector<float>::iterator it=(cpyply->ppg).begin();it!=(cpyply->ppg).end();it++)
        (this->ppg).push((cpyply->ppg)[i]);
}

Player::~Player()
{
}

void update()
{
    //THIS FUNCTION WILL DO API CALLS TO UPDATE THE PLAYER'S STATS
}

vector<float> getStats()
{
    switch(this->pos)
    {
        case 0:
            cerr << "PLAYER DOES NOT EXIST\n";
        case 1:
            //do stuff
        case 2:
            //do stuff
        case 3:
            //do stuff
        /*..........*/
        case default:
            cerr << "DANGER, DANGER WILL ROBINSON! PLAYER DOES NOT EXIST\n"
    }
}
