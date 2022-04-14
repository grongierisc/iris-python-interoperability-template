Class dc.Demo.Production Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="dc.Demo.Production" TestingEnabled="true" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="dc.Demo.RedditService" Category="" ClassName="dc.Demo.RedditService" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Feed">/new/</Setting>
    <Setting Target="Adapter" Name="SSLConfig">default</Setting>
    <Setting Target="Adapter" Name="CallInterval">15</Setting>
    <Setting Target="Adapter" Name="Limit">50</Setting>
  </Item>
  <Item Name="FilterPosts" Category="" ClassName="EnsLib.MsgRouter.RoutingEngine" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="BusinessRuleName">dc.Demo.FilterPostsRoutingRule</Setting>
  </Item>
  <Item Name="dc.Demo.EmailOperation" Category="" ClassName="dc.Demo.EmailOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Adapter" Name="SMTPPort"></Setting>
    <Setting Target="Adapter" Name="SMTPServer"></Setting>
    <Setting Target="Adapter" Name="SSLConfig"></Setting>
    <Setting Target="Adapter" Name="From"></Setting>
    <Setting Target="Adapter" Name="Credentials"></Setting>
  </Item>
  <Item Name="dc.Demo.FileOperation" Category="" ClassName="dc.Demo.FileOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">Path=/irisdev/app/output/</Setting>
  </Item>
  <Item Name="Python.FileOperation" Category="" ClassName="Python.FileOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">Path=/irisdev/app/output/</Setting>
  </Item>
  <Item Name="Python.FileOperationWithIrisAdapter" Category="" ClassName="Python.FileOperationWithIrisAdapter" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="Charset">utf-8</Setting>
    <Setting Target="Adapter" Name="FilePath">/irisdev/app/output/</Setting>
    <Setting Target="Host" Name="%settings">Path=/irisdev/app/output/</Setting>
  </Item>
  <Item Name="Python.EmailOperation" Category="" ClassName="Python.EmailOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="SMTPPort"></Setting>
    <Setting Target="Adapter" Name="SMTPServer"></Setting>
    <Setting Target="Adapter" Name="SSLConfig"></Setting>
    <Setting Target="Adapter" Name="From"></Setting>
    <Setting Target="Adapter" Name="Credentials"></Setting>
  </Item>
  <Item Name="Python.EmailOperationWithIrisAdapter" Category="" ClassName="Python.EmailOperationWithIrisAdapter" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="true" Schedule="">
    <Setting Target="Adapter" Name="SMTPPort"></Setting>
    <Setting Target="Adapter" Name="SMTPServer"></Setting>
    <Setting Target="Adapter" Name="SSLConfig"></Setting>
    <Setting Target="Adapter" Name="From"></Setting>
    <Setting Target="Adapter" Name="Credentials"></Setting>
  </Item>
  <Item Name="Python.RedditService" Category="" ClassName="Python.RedditService" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%classpaths">/irisdev/app/src/python/Reddit|/irisdev/app/src/python/Demo</Setting>
    <Setting Target="Host" Name="%settings">Limit=10</Setting>
  </Item>
  <Item Name="Python.RedditServiceWithIrisAdapter" Category="" ClassName="Python.RedditServiceWithIrisAdapter" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Adapter" Name="Feed">/new/</Setting>
    <Setting Target="Adapter" Name="Limit">4</Setting>
    <Setting Target="Adapter" Name="SSLConfig">default</Setting>
  </Item>
  <Item Name="Python.RedditServiceWithPexAdapter" Category="" ClassName="Python.RedditServiceWithPexAdapter" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Adapter" Name="%settings">Limit=3</Setting>
  </Item>
  <Item Name="Python.FilterPostRoutingRule" Category="" ClassName="Python.FilterPostRoutingRule" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
  </Item>
</Production>
}

}
