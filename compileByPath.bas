Option Explicit
Sub OptionCompile()

Dim FolderPath As String
Dim PathCountCondition As String
Dim FileName As String
Dim Count As Integer
Dim FileNumber As Integer
Dim MainWB As Workbook
Dim WB As Workbook
Dim Rng As Range
Dim RngNoPath As String
Dim StartTime As Double
Dim SecondsElapsed As Double
Dim tickersPerSec As Double

StartTime = Timer

'set this workbook as the main workbook

Set MainWB = ActiveWorkbook
MainWB.Sheets.Add.Name = "DataSet"
MainWB.Sheets.Add.Name = "PathSet"
Set Rng = Range("A1")

Application.DisplayAlerts = False

'define folder path
FolderPath = "C:\Users\m4k04\Desktop\workspace\ipoNotice\option_dfs"

'count number of CSVs in folder

PathCountCondition = FolderPath & "\*.csv"

FileName = Dir(PathCountCondition)

Do While FileName <> ""
    Count = Count + 1
    FileName = Dir()
    Rng.Value = FileName
    Rng.Offset(1, 0).Select
    Set Rng = ActiveCell
Loop

Worksheets("PathSet").Activate
Set Rng = Range("A1")
Rng.Select
Range(Selection, Selection.End(xlDown)).Select
Count = Selection.Rows.Count

Rng.Select

For FileNumber = 1 To Count 'you can change count to a constant for sample runs
    
    'open the file
    
    FileName = FolderPath & "\" & Rng
    
    Set WB = Workbooks.Open(FileName)
    
    'copy its contents
    
    WB.Activate
    Range("A1").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy

    'activate DataSet wrksht and paste data into it
    MainWB.Activate
    Worksheets("DataSet").Activate
    If IsEmpty(Range("A1")) = True Then
        Range("A1").Select
        ActiveSheet.Paste
        Range("A1").Select
    Else
        Range("A1").Select
        Selection.End(xlDown).Select
        Selection.Offset(1, 0).Select
        ActiveSheet.Paste
        Range("A1").Select
    End If
    
    'close file
    WB.Close
    
    'Worksheets("PathSet").Activate
    
    Worksheets("PathSet").Activate
    Rng.Offset(1, 0).Select
    Set Rng = ActiveCell
    
Next FileNumber
                                        
'tell me how long it took
'SecondsElapsed = Round(Timer - StartTime, 2)
'tickersPerSec = Round(Count / SecondsElapsed, 2)
'MsgBox "This code ran successfully in " & SecondsElapsed & " seconds" & vbCrLf & "Approximately " & tickersPerSec & "per second", vbInformation
           

End Sub
