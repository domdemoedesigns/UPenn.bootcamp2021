Sub stocks()
    'Define worksheet as variable
    Dim ws As Worksheet

    'Loop through worksheets in file
    For Each ws In Worksheets

    'Variables
    Dim Ticker As String
    Dim lastRow1 As Long 'Column A
    Dim lastRow2 As Long 'Column K
    'Dim tickerRow As Double
    Dim stockVolume As Double
    Dim summaryTable As Long
    Dim openingPrice As Double
    Dim closingPrice As Double
    Dim yearlyChange As Double
    Dim previousAmount As Long
    Dim percentChange As Double

    'Set counters to default
    summaryTable = 2 'where I'm printing values to
    stockVolume = 0
    previousAmount = 2

    'Column headers and tables returns a range value
    ws.Range("I1").Value = "Ticker"
    ws.Range("J1").Value = "Yearly Change"
    ws.Range("K1").Value = "Percent Change"
    ws.Range("L1").Value = "Total Stock Volume"

    'Finding the last row
    lastRow1 = ws.Cells(Rows.Count, 1).End(xlUp).Row

    'Begin loop
    For i = 2 To lastRow1

        'Add values to stock volume row
        stockVolume = stockVolume + ws.Cells(i, 7).Value

        'Check if the next row has the same values as the previous
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then

            'Set ticker names
            Ticker = ws.Cells(i, 1).Value
            
            'Print ticker name, column I
            ws.Range("I" & summaryTable).Value = Ticker

            'Print total stock volume, colum L
            ws.Range("L" & summaryTable).Value = stockVolume

            'Reset total stock volume
            stockVolume = 0

            'Set yearly opening price
            openingPrice = ws.Range("C" & previousAmount)

            'Set yearly closing price
            closingPrice = ws.Range("F" & i)

            'Set value of yearly change
            yearlyChange = closingPrice - openingPrice
            ws.Range("J" & summaryTable).Value = yearlyChange

            'Determine percent change
            If openingPrice = 0 Then
                percentChange = 0

                'Set percent change to yearly change divided by opening price
                Else
                yearlyOpen = ws.Range("C" & previousAmount)
                percentChange = yearlyChange / openingPrice

            End If

            'Print percent change to column k
            ws.Range("K" & summaryTable).Value = percentChange

            'Conditional formatting, positive to green
            If ws.Range("J" & summaryTable).Value >= 0 Then
            ws.Range("J" & summaryTable).Interior.ColorIndex = 4

                'Condition formatting, negative to red
                Else
                ws.Range("J" & summaryTable).Interior.ColorIndex = 3

            End If

            'Iterate through summary table
            summaryTable = summaryTable + 1

            'set previous amount
            previousAmount = i + 1

        End If

        'Go to next row
        Next i

    Next ws
End Sub
