#include"ode_rk4.h"
#include<iostream>

const float h = 0.000001;
float k1,k2,k3,k4;

float model(/*parameters*/float y, float t, float* args)
{
    float dydt;
    dydt = y* args[0] + args[1];
    return dydt;
}

float rk4(float f, float start_time, float end_time, float *args)
{
    k1 = 0;
    k2 = 0;
    k3 = 0;
    k4 = 0;
    // std::cout<<"start time --> "<<start_time<<"\n";
    while(start_time<end_time)
    {
        k1 = h * model(f,start_time, args);
        start_time = start_time + h*0.5;
        k2 = h * model(f + k1*0.5, start_time, args);
        k3 = h * model(f + k2*0.5, start_time, args);
        start_time = start_time + h*0.5;
        k4 = h * model(f + k3, start_time, args);
        f = f + (k1/6) + (k2/3) + (k3/3) + (k4/6);
        //std::cout<<"time --> "<<start_time<<" k1 / k2 / k3 / k4 --> "<<k1<<" / "<<k2<<" / "<<k3<<" / "<<k4<<"\n";
    }
    // std::cout<<"end time --> "<<end_time<<"\n";
    return f;
}

void allocate_mem(float** y, float** t, float start_time, float end_time, unsigned int size)
{
    float *tf = new float[size];
    tf[0] = start_time;

    float *yf = new float[size];
    yf[0] = 0.0;

    float step = (end_time - start_time) / (size - 1);

    for(/*unsigned */int i=1;i<size;i++)
    {
        start_time = start_time + step;
        // std::cout<<i<<" test "<<start_time<<"\n";
        tf[i] = start_time;
        yf[i] = 0.0;
    }
    *t = tf;
    *y = yf;

}

int main ()
{
    // define arguments to the model
    float *args = new float[2];
    args[0] = 2.0;
    args[1] = 1.5;

    // define start_time, end_time, and resolution sample points for memory allocation
    float start_time = 0.0;
    float end_time = 5.0;
    unsigned int resolution = 100;

    float *t, *y;
    allocate_mem(&y,&t,start_time,end_time,resolution);

    // for(unsigned int i=0;i<resolution;i++)
    // {
    //     std::cout<<t[i]<<"\n";
    // }

    y[0] = 0.1;
    for(unsigned int i=1;i<resolution;i++)
    {
        y[i] = rk4(y[i-1],t[i-1],t[i], args);
        //std::cout<<"the value at time "<<t[i]<<"th sec is --> "<<y[i]<<"\n";
        std::cout<<y[i]<<"\n";
    }

    delete[] y;
    delete[] t;

    return 0;
}
