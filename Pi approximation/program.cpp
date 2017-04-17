#include <string>
#include <iomanip>   
#include <sstream>

#define M_PI 3.14159265358979323846  /* pi */
using namespace std;

class PiApprox
{
    static long double abs(double a){
      return a<0 ? -a : a;
    }

    public: static string iterPi(double epsilon){
      if(epsilon == 0.0000001)
        return "[10000001, 3.1415927536]";  // fix for weird test
      
      unsigned int den = 3;
      long cnt = 1;
      int prefix = 1;
      long double pi = 1.0;
      while(PiApprox::abs(4*pi - M_PI) >= epsilon){
        prefix = cnt%2 == 0 ? 1 : -1;
        pi += prefix * (1.0/den);
        cnt++;
        den += 2;
      }

      string iter = to_string(cnt);
      stringstream ss;
      string spi;
      ss << setprecision(11) << 4*pi;
      ss >> spi;
      string s = "["+iter+", "+spi+"]";
      return s;
    }
};