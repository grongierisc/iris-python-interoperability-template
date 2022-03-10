Class PEX.FileOperation Extends Grongier.PEX.BusinessOperation [ GeneratedBy = Grongier.PEX.Utils ]
{

Parameter ADAPTER = "EnsLib.File.OutboundAdapter";

Parameter SETTINGS = "%classname:Python,%module:Python,%settings:Python,%classpaths:Python";

Property %classname As %String [ InitialExpression = "FileOperation", Internal ];

/// One or more Classpaths (separated by '|' character) needed in addition to the ones configured in the Remote Gateway
Property %classpaths As %String(MAXLEN = "") [ InitialExpression = "/irisdev/app/src/python/Demo" ];

Property %module As %String [ InitialExpression = "FileOperationWithIrisAdaptor", Internal ];

Method SetPropertyValues()
{
	quit
}

}
