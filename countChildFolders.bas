Sub countChildFolders()

    Dim Rng As Range

    Dim oFSO As Object
    Dim folder As Object
    Dim subfolders As Object
    
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
    
End Sub
Sub pickles()

Dim MainWB As Workbook, WB As Workbook
Dim FileName As String

Dim Rng As Range, cell As Range, TrtRng As Range
Dim FilePath As String

Dim Ticker As String
Dim DateExp As Date


Set MainWB = ActiveWorkbook

Set Rng = Range("A1")
Rng.Offset(0, 1).Select
Range(Selection, Selection.End(xlToRight)).Select
Set TrgtRng = Selection

    For Each cell In TrgtRng
        FilePath = Rng & "\" & cell
        Set WB = Workbooks.Open(FilePath)
        Ticker = Range("B2")
        DateExp = Range("C2")
        MsgBox Ticker
        MsgBox DateExp
        'generate code name based off  of ticker and expiry
        
        'if sheet with code name does not exist in MainWB
            'create sheet with code name in MainWB
            'copy data from WB
            'paste data into code named sheet in MainWB
            'close document WB
        
        'if sheet with code name does exist in MainWB
            'activate sheet with code name in MainWB
            'copy data from WB
            'paste data into code named sheet in MainWB
            'close document WB
    Next


End Sub

