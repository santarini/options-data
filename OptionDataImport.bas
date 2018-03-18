Sub OptionDataImport()
    Dim Rng As Range

    Dim oFSO As Object
    Dim folder As Object
    Dim subfolders As Object
    
    Set Rng = Range("A1")
    Set oFSO = CreateObject("Scripting.FileSystemObject")
    Set folder = oFSO.GetFolder("C:\Users\santa\Desktop\option_dfs")
    Set subfolders = folder.subfolders
    For Each Subfolder In folder.subfolders
        Rng.Value = Subfolder
        Rng.Offset(1, 0).Select
        Set Rng = Selection
    Next
    

End Sub
Sub childfolder()
Dim Rng As Range
Dim TrtRng As Range


Dim oFSO As Object
Dim folder As Object
Dim subfolders As Object
Dim PathCount As Integer
Dim FileCount As Integer
Dim i As Integer
Dim FolderPath As String
Dim PathCountCondition As String

Set Rng = Range("A1")

Rng.Select
Range(Selection, Selection.End(xlDown)).Select
PathCount = Selection.Rows.count
For i = 1 To PathCount
    Rng.Select
    Set TrgtRng = Rng.Offset(0, 1)
    FolderPath = Rng.Value
    PathCountCondition = FolderPath & "\calls\*.csv"
    Filename = Dir(PathCountCondition)
    Do While Filename <> ""
        Filename = Dir()
        TrgtRng.Value = Filename
        TrgtRng.Offset(0, 1).Select
        Set TrgtRng = ActiveCell
    Loop
    Set Rng = Rng.Offset(1, 0)
Next i
    



End Sub
Sub countChildFolders()

End Sub

'list child call folder

'list child put folder

'for each child CSV file
'create sheet
'import into Excel
