Sub cheese()

Dim MainWB As Workbook
Dim FileNumber As Integer


Set MainWB = ActiveWorkbook
MainWB.Sheets.Add.Name = "PathSet"

'get paths

Set Rng = Range("C1")
Rng.Select
Range(Selection, Selection.End(xlDown)).Select
RowsCount = Selection.Rows.Count

'
For FileNumber = 1 To RowsCount 'you can change count to a constant for sample runs
    
    'open the file
    
    Filename = FolderPath & "\" & Rng
    
    Set WB = Workbooks.Open(Filename)
    
    'copy its contents
    
    WB.Activate
    Range("A1").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy

    'create new sheet, and paste it into the main workbook
    
    MainWB.Activate
    RngNoPath = Left(Rng, Len(Rng) - 4)
    MainWB.Sheets.Add.Name = RngNoPath
    Range("A1").Select
    ActiveSheet.Paste
    Selection.Columns.AutoFit
    Range("A1").Select
    
    'close file
    WB.Close
    
    Call orderDataForGraphing
    Call manipulateData
    
    'POPULATE SUMMARY PAGE HERE
    Call populateSummary(SummaryRng)
    Worksheets("Summary").Activate
    SummaryRng.Offset(1, 0).Select
    Set SummaryRng = Selection
    
    'Worksheets("PathSet").Activate
    
    Worksheets("PathSet").Activate
    Rng.Offset(1, 0).Select
    Set Rng = ActiveCell
    
Next FileNumber


End Sub
