using System;
interface IMovable
{
    void Move();

}

class Machine {
  public void Start(){
    Console.WriteLine("Machine is starting");
  }
}
class Robot : Machine, IMovable{
    public void Move(){
        Console.WriteLine("Robot is moving");


    }}

    class Program{
        static void Main(){
            Robot r = new Robot();
            r.Start();
            r.Move();
        }
    }