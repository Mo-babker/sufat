Output "preview.gif"

Set FontSize 18
Set Width 1000
Set Height 600
Set Theme "OneDark"

# Start the Python script
Type "python SUFAT.py" Enter
Sleep 1s

# --- Input for 2 Subscribers ---
# 1. Enter number of subscribers
Type "2" Enter
Sleep 0.5s

# --- First Subscriber (Residential - Konut) ---
# 2. Enter subscriber type (1: Konut)
Type "1" Enter
Sleep 0.5s

# 3. Previous meter reading
Type "100" Enter
Sleep 0.5s

# 4. Current meter reading (25 tons used)
Type "125" Enter
Sleep 0.5s

# 5. Previous date
Type "2024-09-01" Enter
Sleep 0.5s

# 6. Current date (30 days later)
Type "2024-10-01" Enter
Sleep 1s

# --- Second Subscriber (Commercial - İş Yeri) ---
# 7. Enter subscriber type (2: İş Yeri)
Type "2" Enter
Sleep 0.5s

# 8. Previous meter reading
Type "50" Enter
Sleep 0.5s

# 9. Current meter reading (15 tons used)
Type "65" Enter
Sleep 0.5s

# 10. Previous date
Type "2024-10-01" Enter
Sleep 0.5s

# 11. Current date (14 days later)
Type "2024-10-15" Enter
Sleep 1s

# --- Analysis Phase ---
# 12. View details and tables?
Type "evet" Enter
Sleep 1s

# 13. Step 1: View Abone Tipi Bilgiler
Type "" Enter
Sleep 1s

# 14. Step 2: View Pie Chart
Type "" Enter
Sleep 1s

# 15. Step 3: View Max Su Tüketim Abone
Type "" Enter
Sleep 0.5s
Type "" Enter
Sleep 1s

# 16. Step 4: View Max Atık Su Ücreti Abone
Type "" Enter
Sleep 0.5s
Type "" Enter
Sleep 1s

# 17. Step 5: View Toplam Su Tüketim Miktarı Bar Chart
Type "" Enter
Sleep 1s

# 18. Step 6: View Toplam Su Tüketim Ücreti Bar Chart
Type "" Enter
Sleep 1s

# 19. Step 7: View Total Wastewater Fee
Type "" Enter
Sleep 1s

# 20. Step 8: View Total VAT
Type "" Enter
Sleep 2s

# End of session
Type "Program completed successfully ✅" Enter
Sleep 1s
