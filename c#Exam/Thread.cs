using System;
public sealed class ConfigurationManager
{
    private static readonly object padlock=new object();
    private static ConfigurationManager instance=null;
    public string Configuration {get; private set;}
    private ConfigurationManager()
    {
        
        Configuration = "Default Configuration";
    }

    public static ConfigurationManager Instance
    {
        get
        {
            lock (padlock)
            {
                if (instance==null)
                {
                    instance=new ConfigurationManager();
                }
                return instance;
            }
        }
    }
}