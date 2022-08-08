#include"ode_rk4.h"
#include<iostream>

const float h = 0.00001;
float k1,k2,k3,k4;

float model(/*parameters*/float y, float t)
{
    float dydt;
    dydt = y*2;
    return dydt;
}

float rk4(float f, float start_time, float end_time)
{
    k1 = 0;
    k2 = 0;
    k3 = 0;
    k4 = 0;
    // std::cout<<"start time --> "<<start_time<<"\n";
    while(start_time<end_time)
    {
        k1 = h * model(f,start_time);
        start_time = start_time + h*0.5;
        k2 = h * model(f + k1*0.5, start_time);
        k3 = h * model(f + k2*0.5, start_time);
        start_time = start_time + h*0.5;
        k4 = h * model(f + k3, start_time);
        f = f + (k1/6) + (k2/3) + (k3/3) + (k4/6);
        //std::cout<<"time --> "<<start_time<<" k1 / k2 / k3 / k4 --> "<<k1<<" / "<<k2<<" / "<<k3<<" / "<<k4<<"\n";
    }
    // std::cout<<"end time --> "<<end_time<<"\n";
    return f;
}

int main ()
{
    float* t = new float[10];
    for(unsigned int i=0;i<10;i++)
        t[i] = (float)i;

    float* y = new float[10];
    y[0] = 0.1;
    for(unsigned int i=1;i<10;i++)
    {
        y[i] = rk4(y[i-1],t[i-1],t[i]);
        std::cout<<"the value at time "<<t[i]<<"th sec is --> "<<y[i]<<"\n";
    }

    return 0;
}
