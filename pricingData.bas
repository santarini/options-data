Sub pricingData()

Application.ScreenUpdating = False

Dim ticker As String
Dim latestPrice As Variant
Dim Json As Object
Dim Dict As New Dictionary

ticker = "AAPL"

Dict.CompareMode = CompareMethod.TextCompare
Dict("A") = ticker

'fetch the url
Set MyRequest = CreateObject("WinHttp.WinHttpRequest.5.1")
MyRequest.Open "GET", "https://api.iextrading.com/1.0/stock/market/batch?symbols=" & ticker & "&types=company,quote"
MyRequest.Send

Set Json = JsonConverter.ParseJson(MyRequest.ResponseText)

latestPrice = Json(Dict.Item("A"))("quote")("latestPrice")

MsgBox latestPrice

End Sub
