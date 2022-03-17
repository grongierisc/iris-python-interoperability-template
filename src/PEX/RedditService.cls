Class PEX.RedditService Extends Grongier.PEX.BusinessService [ GeneratedBy = Grongier.PEX.Utils ]
{

Parameter ADAPTER = "PEX.RedditInboundAdapter";

Parameter SETTINGS = "%classname:Python_Service,%module:Python_Service,%settings:Python_Service,%classpaths:Python_Service";

Property %classname As %String [ InitialExpression = "RedditService", Internal ];

/// One or more Classpaths (separated by '|' character) needed in addition to the ones configured in the Remote Gateway
Property %classpaths As %String(MAXLEN = "") [ InitialExpression = "/irisdev/app/src/python/Demo" ];

Property %module As %String [ InitialExpression = "RedditService", Internal ];

Method SetPropertyValues()
{
	quit
}

}
