Class PEX.RedditInboundAdapter Extends Grongier.PEX.InboundAdapter [ GeneratedBy = Grongier.PEX.Utils ]
{

Parameter SETTINGS = "%classname:Python,%module:Python,%settings:Python,%classpaths:Python";

Property %classname As %String [ InitialExpression = "RedditInboundAdapter", Internal ];

/// One or more Classpaths (separated by '|' character) needed in addition to the ones configured in the Remote Gateway
Property %classpaths As %String(MAXLEN = "") [ InitialExpression = "/irisdev/app/src/python/Reddit" ];

Property %module As %String [ InitialExpression = "InboundAdapter", Internal ];

Method SetPropertyValues()
{
	quit
}

}
