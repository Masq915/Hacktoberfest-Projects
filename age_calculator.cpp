#include<iostream>

using namespace std;

int main()
{
    const int cdate = 23, cmonth = 8, cyear = 2019;
    int bdate, bmonth, byear;
    int fdays{}, fmonth, fyear;
    int monthDays[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};

    //Taking inputs
    cout<<"--------------\n";
    cout<<"Age Calculator\n";
    cout<<"--------------\n";
    cout<<"Enter your birth year -> ";
    cin>>byear;
    cout<<"Enter your birth month -> ";
    cin>>bmonth;
    cout<<"Enter your birth date -> ";
    cin>>bdate;

    //Calculating Year
    fyear = cyear - byear;
    //Calculating Month
    fmonth = cmonth - bmonth;
    if(fmonth<0)
    {
        fmonth += 12;
        fyear--;
    }
    //Calculating Date
    fdays = cdate - bdate;    
    if(fdays<0)
    {
        fdays += 31;
        fmonth--;
    }    
    cout<<"You are...\n";
    cout<<fdays<<" days old\n";
    cout<<fmonth<<" months old\n";
    cout<<fyear<<" years old\n";
    return 0;
}
