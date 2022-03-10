Class PEX.RedditService Extends Grongier.PEX.BusinessService [ GeneratedBy = Grongier.PEX.Utils ]
{

Parameter ADAPTER = "dc.Reddit.InboundAdapter";

Parameter SETTINGS = "%classname:Python,%module:Python,%settings:Python,%classpaths:Python";

Property %classname As %String [ InitialExpression = "RedditService", Internal ];

/// One or more Classpaths (separated by '|' character) needed in addition to the ones configured in the Remote Gateway
Property %classpaths As %String(MAXLEN = "") [ InitialExpression = "/irisdev/app/src/python/Demo" ];

Property %module As %String [ InitialExpression = "RedditServiceWithIrisAdaptor", Internal ];

Method SetPropertyValues()
{
	quit
}

}