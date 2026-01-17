# bosch-ebike-charging
Charge bosch ebike (should work with other brands too) to specific value with shelly plug s and NodeRED

What is needed:
- Switchable power socket that can meassure the power the ebike charger consumes
- NodeRED

Necessary adoptions:
- The function to get the state of the battery from the power the charger consumes must be adapted in the function block "CalculateLoadState" for each ebike individually.
- Maybe the idle power consumption of the charger needs to be adapted so it will be switched of when 100% load are reached

Current limitations:
- Flow can only handle the rising part of the charging curve. As soon as the power consumption drops (from approx. 90% onwards), incorrect values are displayed. 100% charging is possible. To achieve this, the flow waits until the power consumption is just above the idle power consumption of the charger.
- Most probably way more I don't know about yet

How to get the charging curve:
1.) Take screenshots. Example for Shelly Plug S monitored in Home Assistand and charging state from bosch flow app is shown in folder Ladekurve/exampleScreenshots/
2.) arch linux: sudo pacman -S python-pytesseract tesseract tesseract-data-deu tesseract-data-eng python-pandas
3.) python convertScreenshotsToCsv.py (path to tesseract and to screenshots must be adapted)
