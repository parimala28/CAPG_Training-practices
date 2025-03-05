using System;
sealed class SecuritySystem{
    public void AuthenticateUser(){
        Console.WriteLine("User Authentication.");
    }
}
// class paa : SecuritySystem{
//     Console.WriteLine("pp");
// }
class Program{
    static void Main(){
        SecuritySystem ss=new SecuritySystem();
        ss.AuthenticateUser();
    }
}