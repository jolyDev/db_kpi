### C# StartUp
*in this tutorial we will show how to build basic app with visual studio code, 
but if you`re using microsoft visual studio this link might be helpfull 
https://docs.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-5.0&tabs=visual-studio*
+ ##### Open terminal and execute following commands
    + Create a new C# project
        ```csharp
        dotnet new console
        dotnet run
        ```
    + Download required packages
        ```csharp
        dotnet add package Grpc.Net.Client
        dotnet add package Google.Protobuf
        dotnet add package Grpc.Tools
         ```
    + Create new folder in project root directory and name it "protos"
    + Paste *.proto files into "protos" directory
    + Put these lines into your *.csproj file just before "</Project>" tag
        ```xml
          <ItemGroup>
            <Protobuf Include="protos\*.proto" ProtoRoot="protos" GrpcServices="Client" />
          </ItemGroup>
        ```
    + Make sure everything is ok by
    `dotnet build`
+ ##### Client code
    + Paste a following code into your Project.cs
        ```python
        using System;
        using System.Threading.Tasks;
        using Materialise;
        using Grpc.Net.Client;
        
        namespace gRPC_csharp
        {
            class Program
            {
                static async Task Main(string[] args)
                {
                    AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
        
                    using var channel = GrpcChannel.ForAddress("http://localhost:29431");
        
                    {
                        var sg_client_queries = new SupportGenerationQueries.SupportGenerationQueriesClient(channel);
                        var parameters = await sg_client_queries.GetDefaultParametersAsync(new DefaultParametersRequest{});
                    
                        Console.WriteLine(parameters.ToString());
                    }
                }
            }
        }
        ```
    +  Run it
+ ##### More Detailed explanation
    + using Materialise will allow us to use generated csharp code from *.protos
        ``` csharp 
        using Materialise;
        ```
    + Our service runs in a private protected environment which means that we can use http instead of https. We have to explicitly enable this in .NET
        ```csharp
        AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
        ```
