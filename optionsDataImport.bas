Sub countChildFolders()

    Dim Rng As Range

    Dim oFSO As Object
    Dim folder As Object
    Dim subfolders As Object
    
    Application.DisplayAlerts = False
    
    Sheets.Add.Name = "PathSet"
    
    Set Rng = Range("A1")
    Set oFSO = CreateObject("Scripting.FileSystemObject")
    Set folder = oFSO.GetFolder("C:\Users\m4k04\Desktop\option_dfs")
    Set subfolders = folder.subfolders
    For Each Subfolder In folder.subfolders
        Rng.Value = Subfolder
        Rng.Offset(1, 0).Select
        Set Rng = Selection
    Next
    
    Set Rng = Range("A1")
    Set TrgtRng = Rng.Offset(0, 1)
    Rng.Select
    Range(Selection, Selection.End(xlDown)).Select
    PathCount = Selection.Rows.Count
    For i = 1 To PathCount
    Rng.Select
    FolderPath = Rng.Value
    Set folder = oFSO.GetFolder(FolderPath)
    Set subfolders = folder.subfolders
        For Each Subfolder In folder.subfolders
            TrgtRng.Value = Subfolder
            Set TrgtRng = TrgtRng.Offset(1, 0)
        Next
        Set Rng = Rng.Offset(1, 0)
    Next i
    
    Set Rng = Range("B1")

    Rng.Select
    Range(Selection, Selection.End(xlDown)).Select
    PathCount = Selection.Rows.Count
    For i = 1 To PathCount
        Rng.Select
        Set TrgtRng = Rng.Offset(0, 1)
        FolderPath = Rng.Value
        PathCountCondition = FolderPath & "\*.csv"
        FileName = Dir(PathCountCondition)
        Do While FileName <> ""
            FileName = Dir()
            TrgtRng.Value = FileName
            TrgtRng.Offset(0, 1).Select
            Set TrgtRng = ActiveCell
        Loop
        Set Rng = Rng.Offset(1, 0)
    Next i
    
    Columns(1).EntireColumn.Delete
    
    ActiveWorkbook.Worksheets(Worksheets.Count).Delete
    
End Sub
Sub pickles()

Dim MainWB As Workbook, WB As Workbook
Dim FileName As String

Dim Rng As Range, colCell As Range, TrgtRowRng As Range, TrgtColumnRng As Range, rowCell As Range
Dim FilePath As String, Ticker As String, ContractID As String
Dim DateExp As Date

Dim Sht As Worksheet
Dim WorksheetExists As Boolean

Application.DisplayAlerts = False

Set MainWB = ActiveWorkbook

Worksheets("PathSet").Activate
Set colCell = Range("A1")
colCell.Select
Range(Selection, Selection.End(xlDown)).Select
Set TrgtColumnRng = Selection

For Each colCell In TrgtColumnRng
    Worksheets("PathSet").Activate

    colCell.Offset(0, 1).Select
    Range(Selection, Selection.End(xlToRight)).Select
    Set TrgtRowRng = Selection
    For Each rowCell In TrgtRowRng
        FilePath = colCell & "\" & rowCell
        Set WB = Workbooks.Open(FilePath)
        Ticker = Range("C2")
        DateExp = Range("D2")
        ContractID = Ticker & "_" & Format(DateExp, "mmm_yyyy")
        
        'check if worksheets exists
        
        WorksheetExists = False
        
        MainWB.Activate
        For Each Sht In MainWB.Worksheets
            If Sht.Name = ContractID Then
                WorksheetExists = True
            End If
        Next Sht
        
        
        If (WorksheetExists = False) Then
            WB.Activate
            Range("A1").Select
            Range(Selection, Selection.End(xlToRight)).Select
            Range(Selection, Selection.End(xlDown)).Select
            Selection.Copy
            MainWB.Activate
            Sheets.Add.Name = ContractID
            Range("A1").Select
            ActiveSheet.Paste
            Application.CutCopyMode = False
            Range("A1").Select
        End If
        

        If (WorksheetExists = True) Then
            WB.Activate
            Range("A1").Select
            Range(Selection, Selection.End(xlToRight)).Select
            Range(Selection, Selection.End(xlDown)).Select
            Selection.Copy
            MainWB.Activate
            Worksheets(ContractID).Activate
            Range("L1").Select
            ActiveSheet.Paste
            Application.CutCopyMode = False
            Call formatDataFrames
            Call pricingData(Ticker)
            Range("A1").Select
        End If
        WB.Close
    Next
Next
    
    

End Sub

Function formatDataFrames()

'arrange columns and format columns
    Cells.Select
    Selection.Columns.AutoFit
    Columns("O:O").Select
    Selection.Cut
    Columns("W:W").Select
    ActiveSheet.Paste
    Columns("N:N").Select
    Selection.Cut
    Columns("X:X").Select
    ActiveSheet.Paste
    Columns("M:M").Select
    Selection.Cut
    Columns("Y:Y").Select
    ActiveSheet.Paste
    Columns("L:L").Select
    Selection.Cut
    Columns("Z:Z").Select
    ActiveSheet.Paste
    Columns("L:O").Select
    Selection.Delete Shift:=xlToLeft
    Columns("R:R").Select
    Selection.Delete Shift:=xlToLeft
    Range("A1").Select
    
'format numbers
    Columns("E:H").Select
    Selection.Style = "Currency"
    Columns("K:O").Select
    Selection.Style = "Currency"
    Range("A1").Select
    Range("A1:U1").Select
    Selection.Font.Bold = True


End Function

Function pricingData(Ticker As String)


Application.ScreenUpdating = False

Dim latestPrice As Variant
Dim Json As Object
Dim Dict As New Dictionary
Dim Rng As Range
Dim Cell As Range

Dict.CompareMode = CompareMethod.TextCompare
Dict("A") = Ticker


'fetch the url
Set MyRequest = CreateObject("WinHttp.WinHttpRequest.5.1")
MyRequest.Open "GET", "https://api.iextrading.com/1.0/stock/market/batch?symbols=" & Ticker & "&types=company,quote"
MyRequest.Send

Set Json = JsonConverter.ParseJson(MyRequest.ResponseText)

latestPrice = Json(Dict.Item("A"))("quote")("latestPrice")

Set Rng = Range("K1")
Rng.Offset(1, 0).Select
Range(Selection, Selection.End(xlDown)).Select
Set Rng = Selection

For Each Cell In Rng
    If Cell.Value < latestPrice Then
        Cell.Select
        Cell.Offset(0, -10).Resize(1, 10).Select
        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .ThemeColor = xlThemeColorAccent6
            .TintAndShade = 0.399975585192419
            .PatternTintAndShade = 0
        End With
    End If
    If Cell.Value > latestPrice Then
        Cell.Select
        Cell.Offset(0, 1).Resize(1, 9).Select
        With Selection.Interior
            .Pattern = xlSolid
            .PatternColorIndex = xlAutomatic
            .ThemeColor = xlThemeColorAccent6
            .TintAndShade = 0.399975585192419
            .PatternTintAndShade = 0
        End With
    End If
Next Cell

Range("V1") = latestPrice
Range("w1") = Date()

End Function
