@echo off
echo ============================================
echo   TinaTax Form Tests
echo ============================================
echo.
echo Running tests, please wait...
echo.

python -m pytest tests/ -v --csv=results.csv --timeout=30

echo.
echo ============================================
echo   Tests complete! Opening results...
echo ============================================
echo.

start results.csv

pause
