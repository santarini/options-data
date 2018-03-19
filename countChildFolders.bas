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
