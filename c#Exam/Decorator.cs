using System;
public interface ILogger
{
    void Log(string message);
}
public class FileLogger : ILogger
{
    public void Log(string message)
    {
        
        Console.WriteLine($"FileLogger:{message}");
    }
}
public abstract class LoggerDecorator : ILogger
{
    protected ILogger _logger;

    public LoggerDecorator(ILogger logger)
    {
        _logger =logger;
    }

    public virtual void Log(string message)
    {
        _logger.Log(message);
    }
}
public class TimestampLogger : LoggerDecorator
{
    public TimestampLogger(ILogger logger) : base(logger) { }

    public override void Log(string message)
    {
        string timestampedMessage=$"{DateTime.Now}: {message}";
        base.Log(timestampedMessage);
    }
}
public class ErrorCategorizationLogger : LoggerDecorator
{
    public ErrorCategorizationLogger(ILogger logger) : base(logger) { }

    public override void Log(string message)
    {
        string categorizedMessage =$"[Error]: {message}";
        base.Log(categorizedMessage);
    }
}

class Program
{
    static void Main(string[] args)
    {
        ILogger logger =new FileLogger();
        ILogger timestampLogger =new TimestampLogger(logger);
        ILogger errorLogger =new ErrorCategorizationLogger(timestampLogger);

        errorLogger.Log(" test error message.");
    }
}