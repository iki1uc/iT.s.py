#include <iostream>
#define NC_END 25
#define NC_START BOR_EL_ECK
int main(){
 int s[]={1,3,5,7,9}; int t=0;
 for(int n:s){t+=n; std::cout<<t<<" ";}
 std::cout<<"\n"<<NC_END<<"=5*5\n";
 return NC_END-25;
}
